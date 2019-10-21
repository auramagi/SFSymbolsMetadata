import click

from fontTools.ttLib import TTFont
from Cryptodome.Cipher import AES

from base64 import b64decode
from os.path import splitext


@click.command()
@click.argument('filename', type=click.Path(exists=True))
@click.option('--key', prompt='AES Key', help='AES Key used for decryption.')
@click.option('--iv', prompt='AES IV', help='AES IV (initialization vector) used for decryption.')
@click.option('--table_name', default='symp', help='Table name inside TTF/OTF font. Default is \'symp\'.')
@click.option('--out_filename', type=click.Path(dir_okay=False, writable=True), required=False,
              help='Path to write the output. Default is to change FILENAME extension to .csv and append \'-symbols\' '
                   'to the file name.')
def convert(filename, key, iv, table_name, out_filename):
    """
    A tool to decrypt SF Symbols metadata from the font files.
    Reads a TTF/OTF font at FILENAME and outputs the decrypted contents in a file.
    """
    key_b = bytes.fromhex(key)
    iv_b = bytes.fromhex(iv)
    aes = AES.new(key_b, AES.MODE_CBC, iv_b)
    font = TTFont(filename)
    symp = font[table_name].data
    symp_b64 = b64decode(symp)
    csv = aes.decrypt(symp_b64)
    if not out_filename:
        pre, ext = splitext(filename)
        out_filename = pre + '-symbols.csv'
    with open(out_filename, 'wb') as f:
        f.write(csv)
    click.echo('Written %d bytes to %s.' % (len(csv), out_filename))


if __name__ == '__main__':
    convert()

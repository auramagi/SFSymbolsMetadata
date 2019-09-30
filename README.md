# SF Symbols Metadata

## Overview

At **WWDC 2019** Apple announced [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols/overview/), their own set of icons to use in native apps.

The official way to see the full list of provided icons is to use the **SF Symbols app** for macOS.
And this is useful for humans. For computers? Not so much.

The data itself, including symbol names, search metadata, and much more, is baked into *San Francisco* font files in a non-documented private encrypted font table. When decrypted, it happens to be in a nice and easy CSV format.

**SF Symbols Metadata** extracts and decrypts this data.


## Usage

#### CSV files

This repo contains the data extracted from font files. This data is originally in CSV format. Feel free to explore the columns yourself.

All variants of *San Francisco* font contain the same data:  [SFSymbols.csv](/CSV/SFSymbols.csv).

**SF Symbols app** includes a font resource named `SFSymbolsFallback.ttf`, and it contains different data: [SFSymbolsFallback-symbols.csv](/CSV/SFSymbolsFallback-symbols.csv).

#### Conversion script

You can use [sfsymbolsconvert.py](/Script/sfsymbolsconvert.py) to extract the encrypted data contained in *San Francisco* font-family files yourself.

The script uses following dependencies: [Click](https://github.com/pallets/click/), [FontTools](https://github.com/fonttools/fonttools), and [PyCryptodome](https://github.com/Legrandin/pycryptodome). You can install them manually through [pip](https://pip.pypa.io/en/stable/):

```sh
pip3 install click fonttools pycryptodomex
```

Or using [Pipenv](https://github.com/pypa/pipenv):

```sh
pipenv install
pipenv shell
```

Then you can run the script from Terminal like this: `python3 sfsymbolsconvert.py PATH_TO_FONT`. This will ask you to enter the AES Key and IV, see below for Apple values.

```sh
$ python3 sfsymbolsconvert.py SF-Pro-Text-Regular.otf
AES Key: B885F69E398CBA7240DB496BE8C61488549F1F885D476B2E2CC114F13B172120
AES IV: EFB0D12EFAC59114C3E5B91270F0C046
Written 413312 bytes to SF-Pro-Text-Regular-symbols.csv.
```

For further options, run `python3 sfsymbolsconvert.py --help`.

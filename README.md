# Steganography Tool

A simple Python-based steganography tool that encrypts a file (using AES-256) and hides it within an image.

## Features

*   **Strong Encryption**: Uses AES-256 CBC with PKCS7 Padding to encrypt your payload.
*   **Steganography**: Appends the encrypted payload to the end of a cover image.
*   **Decryption & Extraction**: Extracts the encrypted data from the image and decrypts it back to its original form.

## Project Structure

```
Steganography/
├── data/
│   ├── input/                # Place your cover images and files to hide here
│   └── output/               # Generated steganographic images and decrypted files will be saved here
├── src/
│   ├── encrypt.py            # Script to encrypt and hide data
│   └── decrypt.py            # Script to extract and decrypt data
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## Prerequisites

*   Python 3.x
*   Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Configuration**: Open `src/encrypt.py` and `src/decrypt.py` and update the `CONFIGURATION` section to point to your files. The default setup assumes your input files are in `data/input/` and output files will go to `data/output/`.
2.  **AES Key**: Make sure the `AES_KEY` in both scripts is exactly 32 characters long and matches.

### Interactive Menu

The easiest way to use the tool is via the interactive terminal menu:

```bash
python src/main.py
```

### Direct Script Execution

Alternatively, you can still run the scripts directly:

```bash
python src/encrypt.py
```

```bash
python src/decrypt.py
```

## Disclaimer

This tool is for educational purposes only.

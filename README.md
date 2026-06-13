# Steganography Tool

A simple Python-based steganography tool that encrypts a file (using AES-256) and hides it within an image.

## Features

*   **Strong Encryption**: Uses AES-256 CBC with PKCS7 Padding to encrypt your payload.
*   **Steganography**: Appends the encrypted payload to the end of a cover image.
*   **Decryption & Extraction**: Extracts the encrypted data from the image and decrypts it back to its original form.
*   **Interactive CLI**: Beautiful terminal interface with arrow-key navigation (powered by `rich` and `questionary`).

## Project Structure

```
Steganography/
├── data/
│   ├── input/                # Place your cover images and files to hide here
│   └── output/               # Generated steganographic images and decrypted files will be saved here
├── src/
│   ├── main.py               # Main interactive menu script
│   ├── encrypt.py            # Script to encrypt and hide data
│   └── decrypt.py            # Script to extract and decrypt data
├── start.bat                 # Windows quick launch script
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

### Quick Start (Recommended)

The easiest way to use the tool is via the included `start.bat` script, which will automatically install missing dependencies and launch the beautiful interactive terminal menu.

*   **Windows**: Double-click `start.bat` or run from your terminal:
    ```cmd
    start.bat
    ```

### Manual Execution

If you prefer to start the menu manually:

```bash
python src/main.py
```

### Direct Script Execution

Alternatively, you can still run the underlying scripts directly:

```bash
python src/encrypt.py
```

```bash
python src/decrypt.py
```

## Disclaimer

This tool is for educational purposes only.

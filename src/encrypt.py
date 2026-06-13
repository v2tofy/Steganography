import os
from rich.console import Console
console = Console()
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

# ==========================================
#               CONFIGURATION               
# ==========================================

INPUT_FILE_TO_HIDE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "input", "002.exe")       # The file you want to hide
COVER_IMAGE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "input", "001.jpg")               # The normal image used to hide the data
OUTPUT_DATA_IMAGE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "output", "chill Guy.png")# The resulting image with hidden data

# Your fixed 32-character key for AES-256 (Must be exactly 32 characters!)
AES_KEY = "32charkeyforstrongencryption!!!!"

# ==========================================

def encode_data_in_image(img_path, data, output_path):
    """Hides byte data by appending it to the end of an image."""
    with open(img_path, 'rb') as f:
        cover_data = f.read()
        
    # Append the length of the data (8 bytes) at the very end so we can easily extract it
    data_len_bytes = len(data).to_bytes(8, byteorder='big')
    final_data = cover_data + data + data_len_bytes
    
    with open(output_path, 'wb') as f:
        f.write(final_data)
        
    console.print(f"[bold green][*] Saved image to: {output_path}[/bold green]")

def run_encrypt():
    console.print("[bold yellow][*] Starting encryption process...[/bold yellow]")
    
    if not os.path.exists(INPUT_FILE_TO_HIDE):
        console.print(f"[bold red][-] Error: Could not find input file '{INPUT_FILE_TO_HIDE}'. Please create it first.[/bold red]")
        return
    if not os.path.exists(COVER_IMAGE):
        console.print(f"[bold red][-] Error: Could not find cover image '{COVER_IMAGE}'. Please make sure it exists.[/bold red]")
        return

    # 1. Read input file
    with open(INPUT_FILE_TO_HIDE, 'rb') as f:
        file_data = f.read()
        
    # 2. Setup fixed AES-256 key
    key = AES_KEY.encode('utf-8')
    if len(key) != 32:
        console.print(f"[bold red][-] Error: AES_KEY must be EXACTLY 32 characters long for AES-256! (Yours is {len(key)})[/bold red]")
        return
        
    # 3. Encrypt data using AES-256 CBC with PKCS7 Padding
    # This is done so PowerShell can natively decrypt it without third-party tools
    iv = key[:16]
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(file_data) + padder.finalize()
    
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    
    # 4. Hide encrypted data in the first image
    console.print("[bold yellow][*] Hiding AES-256 encrypted data in image...[/bold yellow]")
    encode_data_in_image(COVER_IMAGE, encrypted_data, OUTPUT_DATA_IMAGE)
    
    console.print("\n[bold green][+] Encryption successfully finished.[/bold green]")
    console.print(f"[bold green]    - Data hidden in: {OUTPUT_DATA_IMAGE}[/bold green]")

if __name__ == "__main__":
    run_encrypt()

import os
from rich.console import Console
console = Console()
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

# ==========================================
#               CONFIGURATION               
# ==========================================

DECRYPT_DATA_IMAGE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "output", "chill Guy.png")
DECRYPT_OUTPUT_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "output", "cohost.exe")   # Where to save the recovered file

# Your fixed 32-character key for AES-256 (Must be exactly 32 characters!)
AES_KEY = "32charkeyforstrongencryption!!!!"

# ==========================================

def decode_data_from_image(img_path):
    """Extracts appended byte data from the end of an image."""
    with open(img_path, 'rb') as f:
        content = f.read()
        
    if len(content) < 8:
        raise ValueError("Image file is too small to contain hidden data.")
        
    # Read the last 8 bytes to get the payload length
    data_len = int.from_bytes(content[-8:], byteorder='big')
    
    # Basic validation to ensure the length makes sense
    if data_len > len(content) - 8 or data_len <= 0:
        raise ValueError(f"Invalid data length embedded in image: {data_len}. The image might not contain hidden data.")

    # Extract the exact payload bytes
    payload = content[-8 - data_len : -8]
    return payload

def run_decrypt():
    console.print("[bold yellow][*] Starting decryption process...[/bold yellow]")
    
    if not os.path.exists(DECRYPT_DATA_IMAGE):
        console.print(f"[bold red][-] Error: Could not find data image '{DECRYPT_DATA_IMAGE}'.[/bold red]")
        return

    # 1. Get key from configuration
    console.print("[bold yellow][*] Using AES-256 key from configuration...[/bold yellow]")
    key_data = AES_KEY.encode('utf-8')
    
    if len(key_data) != 32:
        console.print(f"[bold red][-] Error: AES_KEY must be EXACTLY 32 characters long for AES-256! (Yours is {len(key_data)})[/bold red]")
        return
    
    # 2. Extract encrypted data from data image
    console.print("[bold yellow][*] Extracting encrypted data from data image...[/bold yellow]")
    try:
        encrypted_data = decode_data_from_image(DECRYPT_DATA_IMAGE)
    except Exception as e:
        console.print(f"[bold red][-] Error extracting data from image: {e}[/bold red]")
        return
        
    # 3. Decrypt using AES-256 CBC with PKCS7 Padding
    console.print("[bold yellow][*] Decrypting data...[/bold yellow]")
    try:
        iv = key_data[:16]
        cipher = Cipher(algorithms.AES(key_data), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        padded_data = decryptor.update(encrypted_data) + decryptor.finalize()
        
        unpadder = padding.PKCS7(128).unpadder()
        decrypted_data = unpadder.update(padded_data) + unpadder.finalize()
    except Exception as e:
        console.print(f"[bold red][-] Decryption failed! Incorrect key or corrupted data. Error: {e}[/bold red]")
        return
        
    # 4. Save to output file
    with open(DECRYPT_OUTPUT_FILE, 'wb') as f:
        f.write(decrypted_data)
        
    console.print(f"\n[bold green][+] Decryption successful! Hidden file extracted and saved to: {DECRYPT_OUTPUT_FILE}[/bold green]")

if __name__ == "__main__":
    run_decrypt()

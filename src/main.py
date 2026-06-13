import sys
import os
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich.prompt import Prompt
from rich import print as rprint
import questionary
from encrypt import run_encrypt
from decrypt import run_decrypt

console = Console()

def show_banner():
    banner_text = r"""
  ____  _                                                 _           
 / ___|| |_ ___  __ _  __ _ _ __   ___   __ _ _ __ __ _ _ __ | |__  _   _ 
 \___ \| __/ _ \/ _` |/ _` | '_ \ / _ \ / _` | '__/ _` | '_ \| '_ \| | | |
  ___) | ||  __/ (_| | (_| | | | | (_) | (_| | | | (_| | |_) | | | | |_| |
 |____/ \__\___|\__, |\__,_|_| |_|\___/ \__, |_|  \__,_| .__/|_| |_|\__, |
                |___/                   |___/          |_|          |___/ 
    """
    panel = Panel(
        Align.center(Text(banner_text.strip("\n"), style="bold cyan")),
        title="[bold green]Steganography Tool[/bold green]",
        subtitle="[bold yellow]Hide & Extract Data Securely[/bold yellow]",
        border_style="cyan"
    )
    console.print(panel)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    show_banner()
    
    while True:
        try:
            choice = questionary.select(
                "Select an option:",
                choices=[
                    "Encrypt & Hide Data",
                    "Extract & Decrypt Data",
                    "Exit"
                ],
                qmark="",
                instruction=" "
            ).unsafe_ask()
        except KeyboardInterrupt:
            choice = None
            console.print()
        
        if choice == "Encrypt & Hide Data":
            console.print("\n[bold green]=== Encryption Mode ===[/bold green]")
            run_encrypt()
            Prompt.ask("\n[dim]Press Enter to continue[/dim]")
            os.system('cls' if os.name == 'nt' else 'clear')
            show_banner()
        elif choice == "Extract & Decrypt Data":
            console.print("\n[bold blue]=== Decryption Mode ===[/bold blue]")
            run_decrypt()
            Prompt.ask("\n[dim]Press Enter to continue[/dim]")
            os.system('cls' if os.name == 'nt' else 'clear')
            show_banner()
        elif choice == "Exit" or choice is None:
            console.print("\n[bold red]Exiting...[/bold red]")
            break

if __name__ == "__main__":
    main()

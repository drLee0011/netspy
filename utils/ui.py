from colorama import Fore, init
import pyfiglet

init(autoreset=True)

def print_menu(title, options):
    while True:
        print(f"\n=== {title} ===")
        for idx, option in enumerate(options, 1):
            print(f"[{idx}] {option}")
        choice = input("Select an option: ").strip()

        if not choice.isdigit():
            print("❌ Invalid input. Please enter a number.")
            continue

        choice_num = int(choice)
        if 1 <= choice_num <= len(options):
            return choice_num - 1
        else:
            print("❌ Invalid choice. Please select a number from the list.")

def show_welcome():
    ascii_banner = pyfiglet.figlet_format("NetSpy")
    print(Fore.YELLOW + ascii_banner)
    print(Fore.CYAN + "[--] Welcome to NetSpy - Network & Vulnerability Scanner [--]")
    print(Fore.GREEN + "     Created by: Leon")
    print(Fore.MAGENTA + "     Version   : 1.0.0")
    print(Fore.BLUE + "     GitHub    : https://github.com/your-username/netspy")
    print(Fore.YELLOW + "-" * 60)
    print(Fore.GREEN + "NetSpy helps you scan local devices, ports, and detect vulns.")
    print("Use it responsibly and only on networks you have permission to scan!")
    print(Fore.YELLOW + "-" * 60 + "\n")

def confirm_permission():
    confirm = input("⚠️  Do you have permission to scan this network? (y/n): ").strip().lower()
    return confirm == 'y'

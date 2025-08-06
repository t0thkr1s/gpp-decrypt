#!/usr/bin/env python3
"""Command-line interface for gpp-decrypt."""

import argparse
import sys
from pathlib import Path

from colorama import Fore, Style, init

from . import __version__
from .core import decrypt_password, parse_xml_file

# Initialize colorama for cross-platform colored output
init(autoreset=True)

BANNER = """
                              __                                __ 
  ___ _   ___    ___  ____ ___/ / ___  ____  ____  __ __   ___  / /_
 / _ `/  / _ \  / _ \/___// _  / / -_)/ __/ / __/ / // /  / _ \/ __/
 \_, /  / .__/ / .__/     \_,_/  \__/ \__/ /_/    \_, /  / .__/\__/ 
/___/  /_/    /_/                                /___/  /_/         

"""

# Color scheme for output
SUCCESS = Style.BRIGHT + '[ ' + Fore.GREEN + '✓' + Fore.RESET + ' ] ' + Style.RESET_ALL
INFO = Style.BRIGHT + '[ ' + Fore.CYAN + '•' + Fore.RESET + ' ] ' + Style.RESET_ALL
WARNING = Style.BRIGHT + '[ ' + Fore.YELLOW + '!' + Fore.RESET + ' ] ' + Style.RESET_ALL
ERROR = Style.BRIGHT + '[ ' + Fore.RED + '✗' + Fore.RESET + ' ] ' + Style.RESET_ALL


def print_banner():
    """Print the application banner."""
    print(Fore.CYAN + BANNER + Style.RESET_ALL)
    print(f"{INFO}GPP-Decrypt v{__version__} - Group Policy Preferences Password Decryptor")
    print(f"{INFO}Author: Kristof Toth (@t0thkr1s)")
    print()


def decrypt_single_password(cpassword: str) -> None:
    """
    Decrypt and display a single cpassword.
    
    Args:
        cpassword: The encrypted password to decrypt
    """
    try:
        decrypted = decrypt_password(cpassword)
        print(f"{SUCCESS}Decrypted password: {Fore.GREEN}{decrypted}{Style.RESET_ALL}")
    except ValueError as e:
        print(f"{ERROR}Failed to decrypt: {e}")
        sys.exit(1)


def process_xml_file(filepath: str, verbose: bool = False) -> None:
    """
    Process and display credentials from a GPP XML file.
    
    Args:
        filepath: Path to the XML file
        verbose: Whether to show verbose output
    """
    path = Path(filepath)
    
    if not path.exists():
        print(f"{ERROR}File not found: {filepath}")
        sys.exit(1)
    
    if not path.is_file():
        print(f"{ERROR}Not a file: {filepath}")
        sys.exit(1)
    
    print(f"{INFO}Processing file: {filepath}")
    
    try:
        results = parse_xml_file(filepath)
        
        if not results:
            print(f"{WARNING}No encrypted passwords found in the XML file")
            return
        
        print(f"{SUCCESS}Found {len(results)} credential(s)\n")
        
        for idx, cred in enumerate(results, 1):
            print(f"{Fore.YELLOW}═══ Credential #{idx} ═══{Style.RESET_ALL}")
            
            if cred['type'] == 'User':
                print(f"{INFO}Type: User Account")
                print(f"{INFO}Username: {Fore.CYAN}{cred.get('username', 'N/A')}{Style.RESET_ALL}")
            else:
                print(f"{INFO}Type: Group Policy")
                print(f"{INFO}Group: {Fore.CYAN}{cred.get('groupname', 'N/A')}{Style.RESET_ALL}")
                print(f"{INFO}Username: {Fore.CYAN}{cred.get('username', 'N/A')}{Style.RESET_ALL}")
            
            if verbose:
                print(f"{INFO}Encrypted: {cred['encrypted'][:20]}...")
            
            if cred.get('password'):
                print(f"{SUCCESS}Password: {Fore.GREEN}{cred['password']}{Style.RESET_ALL}")
            else:
                error_msg = cred.get('error', 'Unknown error')
                print(f"{ERROR}Password: {Fore.RED}{error_msg}{Style.RESET_ALL}")
            
            print()
            
    except Exception as e:
        print(f"{ERROR}Error processing file: {e}")
        sys.exit(1)


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description='Decrypt Group Policy Preferences passwords',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s -f groups.xml          Decrypt passwords from an XML file
  %(prog)s -c j1Uyj3Vx8TY9LtL...  Decrypt a single cpassword
  %(prog)s -f groups.xml -v       Show verbose output
        """
    )
    
    parser.add_argument(
        '-v', '--version',
        action='version',
        version=f'%(prog)s {__version__}'
    )
    
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Enable verbose output'
    )
    
    parser.add_argument(
        '--no-banner',
        action='store_true',
        help='Suppress the banner'
    )
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        '-f', '--file',
        metavar='FILE',
        help='Path to the GPP XML file (e.g., groups.xml)'
    )
    group.add_argument(
        '-c', '--cpassword',
        metavar='CPASS',
        help='Single cpassword to decrypt'
    )
    
    args = parser.parse_args()
    
    if not args.no_banner:
        print_banner()
    
    if args.cpassword:
        decrypt_single_password(args.cpassword)
    else:
        process_xml_file(args.file, args.verbose)


if __name__ == "__main__":
    main()

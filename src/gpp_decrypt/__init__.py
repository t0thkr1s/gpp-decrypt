"""
GPP-Decrypt: A tool to decrypt Group Policy Preferences cpassword attributes.

This tool parses Group Policy Preferences XML files and decrypts the cpassword
attribute using the publicly known AES key.
"""

__version__ = "2.0.0"
__author__ = "Kristof Toth"
__email__ = "t0thkr1s@icloud.com"

from .core import decrypt_password

__all__ = ["decrypt_password"]

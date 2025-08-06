"""Core decryption functionality for GPP passwords."""

import base64
from typing import Optional
from xml.etree import ElementTree
from xml.etree.ElementTree import ParseError

from Crypto.Cipher import AES


# Microsoft's published AES key for GPP encryption
GPP_AES_KEY = (
    b'\x4e\x99\x06\xe8\xfc\xb6\x6c\xc9\xfa\xf4\x93\x10\x62\x0f\xfe\xe8'
    b'\xf4\x96\xe8\x06\xcc\x05\x79\x90\x20\x9b\x09\xa4\x33\xb6\x6c\x1b'
)
GPP_AES_IV = b'\x00' * 16


def decrypt_password(cpassword: str) -> str:
    """
    Decrypt a GPP cpassword attribute.
    
    Args:
        cpassword: The encrypted password from the GPP XML file
        
    Returns:
        The decrypted password as a string
        
    Raises:
        ValueError: If the cpassword is invalid or decryption fails
    """
    if not cpassword:
        raise ValueError("Empty cpassword provided")
    
    # Add padding if necessary
    padding = '=' * (4 - len(cpassword) % 4)
    padded_cpass = cpassword + padding
    
    try:
        decoded = base64.b64decode(padded_cpass)
    except Exception as e:
        raise ValueError(f"Failed to decode base64: {e}")
    
    # Decrypt using AES-CBC
    cipher = AES.new(GPP_AES_KEY, AES.MODE_CBC, GPP_AES_IV)
    
    try:
        decrypted = cipher.decrypt(decoded)
        # Remove padding and decode
        result = decrypted.decode('utf-16-le').rstrip('\x00')
        return result
    except Exception as e:
        raise ValueError(f"Failed to decrypt password: {e}")


def parse_xml_file(filepath: str) -> dict:
    """
    Parse a GPP XML file and extract credentials.
    
    Args:
        filepath: Path to the XML file
        
    Returns:
        Dictionary containing username and decrypted password
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        ParseError: If the XML is invalid
        ValueError: If required elements are not found
    """
    try:
        tree = ElementTree.parse(filepath)
        root = tree.getroot()
    except ParseError as e:
        raise ParseError(f"Invalid XML file: {e}")
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")
    
    results = []
    
    # Check for User elements
    for user in root.findall('.//User'):
        username = user.get('name')
        properties = user.find('Properties')
        
        if properties is not None:
            cpassword = properties.get('cpassword')
            if cpassword:
                try:
                    password = decrypt_password(cpassword)
                    results.append({
                        'type': 'User',
                        'username': username,
                        'password': password,
                        'encrypted': cpassword
                    })
                except ValueError:
                    results.append({
                        'type': 'User',
                        'username': username,
                        'password': None,
                        'encrypted': cpassword,
                        'error': 'Failed to decrypt'
                    })
    
    # Check for Groups elements
    for group in root.findall('.//Group'):
        groupname = group.get('name')
        properties = group.find('Properties')
        
        if properties is not None:
            username = properties.get('userName')
            cpassword = properties.get('cpassword')
            if cpassword:
                try:
                    password = decrypt_password(cpassword)
                    results.append({
                        'type': 'Group',
                        'groupname': groupname,
                        'username': username,
                        'password': password,
                        'encrypted': cpassword
                    })
                except ValueError:
                    results.append({
                        'type': 'Group',
                        'groupname': groupname,
                        'username': username,
                        'password': None,
                        'encrypted': cpassword,
                        'error': 'Failed to decrypt'
                    })
    
    return results

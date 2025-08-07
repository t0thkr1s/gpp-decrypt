<div align="center">

# 🚀 GPP-Decrypt

**A tool to decrypt Group Policy Preferences (GPP) passwords**

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-GPL%20v3-green?style=for-the-badge)](https://github.com/t0thkr1s/gpp-decrypt/blob/master/LICENSE)
[![Stars](https://img.shields.io/github/stars/t0thkr1s/gpp-decrypt?style=for-the-badge)](https://github.com/t0thkr1s/gpp-decrypt/stargazers)

</div>

![Screenshot](https://i.imgur.com/dn7tNDc.png)

## About

Group Policy Preferences (GPP) was introduced in Windows Server 2008 and allows administrators to set domain passwords via Group Policy. However, the passwords are encrypted with a publicly known AES-256 key, making them trivial to decrypt.

This tool decrypts these passwords from GPP XML files commonly found in SYSVOL shares.

> **Note**: Microsoft released [MS14-025](https://support.microsoft.com/en-us/topic/ms14-025-vulnerability-in-group-policy-preferences-could-allow-elevation-of-privilege-may-13-2014-60734e15-af79-26ca-ea53-8cd617073c30) which prevents new credentials from being stored in GPP. However, existing GPP XML files with encrypted passwords may still exist in many environments.

## Installation

### From PyPI (Recommended)

```bash
pip install gpp-decrypt
```

### From Source

```bash
git clone https://github.com/t0thkr1s/gpp-decrypt.git
cd gpp-decrypt
pip install .
```

### Using Docker

```bash
docker build -t gpp-decrypt .
docker run -v $(pwd):/data gpp-decrypt -f /data/groups.xml
```

## Usage

### Command Line Interface

```bash
# Decrypt passwords from a GPP XML file
gpp-decrypt -f groups.xml

# Decrypt a single cpassword
gpp-decrypt -c "j1Uyj3Vx8TY9LtLZil2uAuZkFQA/4latT76ZwgdHdhw"

# Show verbose output
gpp-decrypt -f groups.xml --verbose

# Suppress banner
gpp-decrypt -f groups.xml --no-banner
```

### As a Python Library

```python
from gpp_decrypt import decrypt_password, parse_xml_file

# Decrypt a single password
password = decrypt_password("j1Uyj3Vx8TY9LtLZil2uAuZkFQA/4latT76ZwgdHdhw")
print(f"Decrypted: {password}")

# Parse and decrypt from XML file
results = parse_xml_file("groups.xml")
for cred in results:
    print(f"Username: {cred['username']}, Password: {cred['password']}")
```

## Example

GPP XML files are typically found in the SYSVOL share of a domain controller:
```
\\<DOMAIN>\SYSVOL\<DOMAIN>\Policies\{<POLICY_GUID>}\Machine\Preferences\Groups\Groups.xml
\\<DOMAIN>\SYSVOL\<DOMAIN>\Policies\{<POLICY_GUID>}\User\Preferences\Groups\Groups.xml
```

Example Groups.xml structure:
```xml
<?xml version="1.0" encoding="utf-8"?>
<Groups clsid="{3125E937-EB16-4b4c-9934-544FC6D24D26}">
  <User clsid="{DF5F1855-51E5-4d24-8B1A-D9BDE98BA1D1}" 
        name="Administrator" 
        image="2" 
        changed="2023-01-01 00:00:00" 
        uid="{EF57DA28-5F69-4530-A59E-AAB58578219D}">
    <Properties action="U" 
                newName="" 
                fullName="" 
                description="" 
                cpassword="j1Uyj3Vx8TY9LtLZil2uAuZkFQA/4latT76ZwgdHdhw" 
                changeLogon="0" 
                noChange="1" 
                neverExpires="1" 
                acctDisabled="0" 
                userName="Administrator"/>
  </User>
</Groups>
```

## References

- [Microsoft's MS14-025 Security Bulletin](https://support.microsoft.com/en-us/topic/ms14-025-vulnerability-in-group-policy-preferences-could-allow-elevation-of-privilege-may-13-2014-60734e15-af79-26ca-ea53-8cd617073c30)
- [Original GPP Decrypt Research](https://labs.portcullis.co.uk/blog/are-you-considering-using-microsoft-group-policy-preferences/)
- [Group Policy Preferences and Getting Your Domain 0wned](https://www.rapid7.com/blog/post/2016/07/27/pentesting-in-the-real-world-group-policy-pwnage/)

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is designed for authorized security testing and system administration only. Users are responsible for complying with all applicable laws and regulations. The authors assume no liability for misuse or damage caused by this program.

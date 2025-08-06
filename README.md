# GPP-Decrypt 🔐

<div align="center">

[![PyPI - Version](https://img.shields.io/pypi/v/gpp-decrypt)](https://pypi.org/project/gpp-decrypt/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/gpp-decrypt)](https://pypi.org/project/gpp-decrypt/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![CI](https://github.com/t0thkr1s/gpp-decrypt/workflows/CI/badge.svg)](https://github.com/t0thkr1s/gpp-decrypt/actions)
[![Downloads](https://pepy.tech/badge/gpp-decrypt)](https://pepy.tech/project/gpp-decrypt)

**A fast and reliable tool to decrypt Group Policy Preferences (GPP) passwords**

<img src="https://i.imgur.com/dn7tNDc.png" alt="GPP-Decrypt Screenshot" width="600"/>

</div>

## 📖 About

Group Policy Preferences (GPP) was introduced in Windows Server 2008 and allows administrators to set domain passwords via Group Policy. However, the passwords are encrypted with a publicly known AES-256 key, making them trivial to decrypt.

This tool helps security professionals and system administrators audit their Group Policy configurations by decrypting these passwords from GPP XML files commonly found in SYSVOL shares.

> **⚠️ Security Notice**: Microsoft released [MS14-025](https://support.microsoft.com/en-us/topic/ms14-025-vulnerability-in-group-policy-preferences-could-allow-elevation-of-privilege-may-13-2014-60734e15-af79-26ca-ea53-8cd617073c30) which prevents new credentials from being stored in GPP. However, existing GPP XML files with encrypted passwords may still exist in many environments.

## ✨ Features

- 🚀 **Fast & Efficient** - Optimized decryption process
- 🎨 **Beautiful CLI** - Colored output with clear formatting
- 📦 **Multiple Formats** - Supports both individual passwords and XML files
- 🔍 **Comprehensive Parsing** - Handles various GPP XML formats (Users, Groups, etc.)
- 🐍 **Modern Python** - Full type hints and Python 3.8+ support
- 🧪 **Well Tested** - Comprehensive test suite with CI/CD
- 📚 **API Access** - Import as a library for your own tools
- 🌍 **Cross-Platform** - Works on Windows, Linux, and macOS

## 📦 Installation

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

## 🚀 Usage

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

## 📁 Example XML Files

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

## 🔧 Development

### Setting up the development environment

```bash
# Clone the repository
git clone https://github.com/t0thkr1s/gpp-decrypt.git
cd gpp-decrypt

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"
```

### Running tests

```bash
# Run tests with coverage
pytest tests/ -v --cov=src/gpp_decrypt

# Run linting
flake8 src/
black --check src/
mypy src/
```

### Building documentation

```bash
# Install documentation dependencies
pip install -e ".[docs]"

# Build documentation
cd docs && make html
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Changelog

See [CHANGELOG.md](CHANGELOG.md) for a detailed list of changes between versions.

## 🔗 References

- [Microsoft's MS14-025 Security Bulletin](https://support.microsoft.com/en-us/topic/ms14-025-vulnerability-in-group-policy-preferences-could-allow-elevation-of-privilege-may-13-2014-60734e15-af79-26ca-ea53-8cd617073c30)
- [Original GPP Decrypt Research](https://labs.portcullis.co.uk/blog/are-you-considering-using-microsoft-group-policy-preferences/)
- [Group Policy Preferences and Getting Your Domain 0wned](https://www.rapid7.com/blog/post/2016/07/27/pentesting-in-the-real-world-group-policy-pwnage/)

## ⚖️ License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool is designed for authorized security testing and system administration only. Users are responsible for complying with all applicable laws and regulations. The authors assume no liability for misuse or damage caused by this program.

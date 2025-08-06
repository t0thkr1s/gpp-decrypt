# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2024-01-XX

### Added
- Complete project restructure for modern Python packaging
- PyPI package support with proper metadata
- Comprehensive test suite with pytest
- GitHub Actions CI/CD pipelines for automated testing and releases
- Type hints throughout the codebase
- Support for both User and Group XML elements
- Verbose output option
- No-banner option for script automation
- Better error handling and reporting
- Cross-platform compatibility improvements
- API access - can be imported as a library
- Docker support

### Changed
- Migrated from pycrypto to pycryptodome for better maintenance
- Improved CLI with better formatting and colors
- Updated minimum Python version to 3.7
- Restructured code into proper package format (src layout)
- Enhanced XML parsing to handle more GPP formats
- Better decryption error messages

### Fixed
- Unicode handling issues
- XML parsing edge cases
- Padding issues with certain cpassword values

### Security
- Updated all dependencies to latest secure versions
- Added security warnings about MS14-025

## [1.0.0] - Initial Release

### Added
- Basic GPP password decryption functionality
- Support for Groups.xml files
- Command-line interface
- Basic colored output

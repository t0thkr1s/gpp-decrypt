"""Tests for the core decryption module."""

import pytest
from gpp_decrypt.core import decrypt_password, parse_xml_file


class TestDecryptPassword:
    """Test cases for password decryption."""
    
    def test_decrypt_valid_password(self):
        """Test decryption of a known valid cpassword."""
        # This is a known test vector: password = "Password1"
        cpassword = "j1Uyj3Vx8TY9LtLZil2uAuZkFQA/4latT76ZwgdHdhw"
        result = decrypt_password(cpassword)
        assert result == "Password1"
    
    def test_decrypt_empty_password(self):
        """Test that empty password raises ValueError."""
        with pytest.raises(ValueError, match="Empty cpassword"):
            decrypt_password("")
    
    def test_decrypt_invalid_base64(self):
        """Test that invalid base64 raises ValueError."""
        with pytest.raises(ValueError, match="Failed to decode base64"):
            decrypt_password("not-valid-base64!@#$")
    
    def test_decrypt_with_padding(self):
        """Test decryption handles padding correctly."""
        # Password without proper padding
        cpassword = "j1Uyj3Vx8TY9LtLZil2uAuZkFQA/4latT76ZwgdHdhw"
        result = decrypt_password(cpassword)
        assert result == "Password1"


class TestParseXmlFile:
    """Test cases for XML file parsing."""
    
    def test_parse_nonexistent_file(self):
        """Test that nonexistent file raises FileNotFoundError."""
        with pytest.raises(FileNotFoundError):
            parse_xml_file("/nonexistent/file.xml")
    
    def test_parse_valid_xml(self, tmp_path):
        """Test parsing a valid GPP XML file."""
        xml_content = """<?xml version="1.0" encoding="utf-8"?>
        <Groups clsid="{3125E937-EB16-4b4c-9934-544FC6D24D26}">
          <User clsid="{DF5F1855-51E5-4d24-8B1A-D9BDE98BA1D1}" 
                name="TestUser" 
                uid="{EF57DA28-5F69-4530-A59E-AAB58578219D}">
            <Properties cpassword="j1Uyj3Vx8TY9LtLZil2uAuZkFQA/4latT76ZwgdHdhw" 
                        userName="TestUser"/>
          </User>
        </Groups>"""
        
        xml_file = tmp_path / "test.xml"
        xml_file.write_text(xml_content)
        
        results = parse_xml_file(str(xml_file))
        assert len(results) == 1
        assert results[0]['type'] == 'User'
        assert results[0]['username'] == 'TestUser'
        assert results[0]['password'] == 'Password1'
    
    def test_parse_invalid_xml(self, tmp_path):
        """Test that invalid XML raises ParseError."""
        xml_file = tmp_path / "invalid.xml"
        xml_file.write_text("This is not valid XML")
        
        from xml.etree.ElementTree import ParseError
        with pytest.raises(ParseError):
            parse_xml_file(str(xml_file))
    
    def test_parse_xml_without_cpassword(self, tmp_path):
        """Test parsing XML without cpassword attributes."""
        xml_content = """<?xml version="1.0" encoding="utf-8"?>
        <Groups clsid="{3125E937-EB16-4b4c-9934-544FC6D24D26}">
          <User clsid="{DF5F1855-51E5-4d24-8B1A-D9BDE98BA1D1}" 
                name="TestUser">
            <Properties userName="TestUser"/>
          </User>
        </Groups>"""
        
        xml_file = tmp_path / "no_cpass.xml"
        xml_file.write_text(xml_content)
        
        results = parse_xml_file(str(xml_file))
        assert len(results) == 0

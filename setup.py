from setuptools import setup

setup(
    name='gpp-decrypt',
    version='1.0',
    author='Kristof Toth',
    author_email='t0thkr1s@icloud.com',
    description='Tool to parse the Group Policy Preferences XML file which '
                'extracts the username and decrypts the cpassword attribute.',
    install_requires=['Crypto', 'colorama']
)

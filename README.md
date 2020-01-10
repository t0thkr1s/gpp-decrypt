# gpp-decrypt

[![made-with-python](http://forthebadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![built-with-love](http://forthebadge.com/images/badges/built-with-love.svg)](https://gitHub.com/t0thkr1s/)

> Note: The idea is heavily based on this project: https://github.com/BustedSec/gpp-decrypt 

This tool is written in Python 3 to parse the Group Policy Preferences XML file which extracts the username and decrypts the cpassword attribute.

## Download

```
git clone https://github.com/t0thkr1s/gpp-decrypt
```

## Install

The script has only 2 dependencies:

*   [pycrypto](https://pypi.org/project/pycrypto/)
*   [colorama](https://pypi.org/project/colorama/)

You can install these by typing:

```
python3 setup.py install
```

## Run

```
python3 gpp-decrypt.py -f [groups.xml]
```
or
```
python3 gpp-decrypt.py -c [cpassword]
```

## Screenshot

![Screenshot](https://i.imgur.com/dn7tNDc.png)

### Disclaimer

> This tool is only for testing and academic purposes and can only be used where strict consent has been given. Do not use it for illegal purposes! It is the end user’s responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this tool and software.

## License

This project is licensed under the GPLv3 License - see the [LICENSE](LICENSE) file for details

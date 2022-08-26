FROM python:3.9-buster
RUN pip3 install pycrypto colorama
ADD gpp-decrypt.py .
ENTRYPOINT [ "python3", "gpp-decrypt.py" ]

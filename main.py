import re

pgp_key = """-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: OpenPGP.js v4.10.10
Comment: https://openpgpjs.org

xsBNBF0GjRABCACyR9mv5xj2ELvSxiEx8EkC4AI+5fFy4xZ45/KDJXpyqKrS
gGoGLjBTnBES1H7PbOm6wHAnR9V7PDCuDF4PL12mYkZyTcoATbN3bAFRz0YL
xP2yDJTzY9eTpTq+ltXz9jmy6t5h7X/jT67CXzSw2MdpJvWAmKltAaRnu/cr
...
68ev3zD0DchLh8SGlJ4F5MTkgvYItR0f4iZeCm6G2Rb06CtMXD5/31R9FwVI
-----END PGP PUBLIC KEY BLOCK-----"""

# ls's regex 
# regex = r"^-----BEGIN PGP PUBLIC KEY BLOCK-----(?:\r?\n)(?:(?:[A-Za-z0-9+/]{4})+(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{4})){1,}(?:\r?\n)-----END PGP PUBLIC KEY BLOCK-----$"

#jer's regex
#regex = "/^(-----BEGIN PGP PUBLIC KEY BLOCK-----).*([a-zA-Z0-9//\n\/\.\:\+\ \=]+).*(-----END PGP PUBLIC KEY BLOCK-----)$"

# print(pgp_key)

regex = re.compile(r'^.*$')#(?:\-{5}BEGIN PGP PUBLIC KEY BLOCK\-{5}).+")#(?:-----END PGP PUBLIC KEY BLOCK-----)")

if regex.match(pgp_key, re.DOTALL | re.MULTILINE):
    print("Valid PGP key")
else:
    print("Invalid PGP key")

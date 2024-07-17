import base64

# 1. ASCII
ords = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
print("Here is your ASCII flag:")
print("".join(chr(o) for o in ords))
## crypto{ASCII_pr1nt4bl3}

# 2. Hex
hexString = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
bytes = bytes.fromhex(hexString)
print(bytes)
## b'crypto{You_will_be_working_with_hex_strings_a_lot}'

# 3. Base64
base64FromHex = base64.b64encode(bytes.fromhex("72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"))
print(base64FromHex)
## b'crypto/Base+64+Encoding+is+Web+Safe/'

# 4. Bytes and Big Integers
# Python's PyCryptodome library implements this with the methods bytes_to_long() and long_to_bytes()
from Crypto.Util.number import *
bytes = long_to_bytes(11515195063862318899931685488813747395775516287289682636499965282714637259206269)
print(bytes)
## b'crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}'
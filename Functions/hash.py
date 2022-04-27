# LIB IMPORTS
import hashlib

# FUNCTION IMPORTS
from Functions.password import fetchPassword

# HASH
def hashData():
    # DATA
    data = fetchPassword()

    # BYTECODE
    bytecode = data.encode()

    # SHA-256 HASH
    sha3code = hashlib.sha3_256(bytecode)

    # HEX HASH
    hashcode = sha3code.hexdigest()
    return hashcode
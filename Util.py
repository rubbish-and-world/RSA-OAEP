import hashlib

# return md4 checksum for given input without length limitation
def MD4(input : bytearray) -> bytearray:
    return bytearray(hashlib.new('md4' , input).digest())

# xor two bytearray
def xor_bytes(a : bytearray ,b : bytearray ) -> bytearray :
    if len(a) != len(b):
        raise Exception("xor length discord")
    return bytearray([_a ^ _b for _a,_b in zip(a,b)])
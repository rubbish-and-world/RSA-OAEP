import Util
import random
from math import ceil
from Primitive import I2OSP

Hash = Util.MD4
hLen = 16  # output length of the Hash function (count in bytes)

def MGF(Z : bytearray ,  l : int) -> bytearray :
    '''
    Options: 
    	Hash hash function (hLen denotes the length in octets of the hash function output) 
	Input:
		Z seed from which mask is generated, an octet string
		l intended length in octets of the mask, at most 2**32*hLen
	Output: 
		mask, an octet string of length l
    '''
    if l > 2**32 * hLen:
        raise Exception("mask too long")
    
    T = bytearray()
    for i in range( ceil(l/hLen) ):
        c = I2OSP(i, 4)
        T += Hash(Z+c)
    return T[:l]

# EME-OAEP-Encode
def OAEP_Encode(M : bytearray, emLen : int) -> bytearray :
    
    mLen = len(M)
    
    if emLen < (2*hLen):
        raise Exception("Intended message length too short")

    if  mLen > (emLen - 2*hLen) :
        raise Exception("message too long")

    seed = random.randbytes(hLen) # generate k bit random value `r`
    DBmask = MGF(seed, emLen - hLen)
    DB = M + b'\x01' + bytearray([0 for i in range(emLen - hLen - mLen - 1)])
    maskedDB = Util.xor_bytes(DB , DBmask)
    seedmask = MGF(maskedDB, hLen)
    maskedseed = Util.xor_bytes(seed , seedmask)
    return maskedseed + maskedDB


# EME_OAEP_Decode
def OAEP_Decode(EM : bytearray ) -> bytearray :
    """
    Input:
    	EM, encoded message
    	
    Output:
    	M , the recovered message
    """
    emLen = len(EM)
    if emLen < (2*hLen) :
        raise Exception("decoding error")
    
    maskedSeed , maskedDB = EM[:hLen] , EM[hLen:]
    seed = Util.xor_bytes(maskedSeed , MGF(maskedDB , hLen))
    DB = Util.xor_bytes(maskedDB , MGF(seed , emLen - hLen))
    message = DB.rstrip(b'\x00')[:-1]
    return message

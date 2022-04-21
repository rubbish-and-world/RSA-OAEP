import Prime
import Primitive
import math
import OAEP
# RSA Key Generation Function
def RSAKG(L : int , e : int ) -> tuple:
    """
    Input: 
    	L, the desired bit length for the modulus
		e, the public exponent, an odd integer greater than 1
    Output:
 		K , a valid private key
        (n,e), a valid public key
    """

    # since (a bits * b bits) gives  max(a,b) bits <= result <= a+b bits
    # the actual key length might be larger than the given size
    p,q = 0,0
    while math.gcd(p, e) != 1:
        p = Prime.Prime(L)
    while math.gcd(q, e) != 1:
        q = Prime.Prime(L)
    
    n = p*q
    phin = math.lcm(p-1 , q-1)
    d = pow(e, -1 , phin)

    return ((n,e),(n,d))



# public len k+m = `k`

# The Encryption Function
def RSA_OAEP_Encrypt(PublicKey : tuple, M  : bytearray ) -> tuple:
    k = (len(M) + OAEP.hLen)*2
    EM = OAEP.OAEP_Encode(M,k)          # Encoded Message
    IM = Primitive.OS2IP(EM)            # Integer Message
    IC = Primitive.RSAEP(PublicKey, IM) # Integer Cipher
    OC = Primitive.I2OSP(IC, 1024)         # OctetString Cipher
    return OC,k

# Then Decryption Function
def RSA_OAEP_Decrypt(PrivateKey : tuple , C : bytearray  , k) -> bytearray:
    IC = Primitive.OS2IP(C) # Integer Cipher
    IM = Primitive.RSADP(PrivateKey, IC) # Integer Message
    EM = Primitive.I2OSP(IM, k)
    DM = OAEP.OAEP_Decode(EM)
    return DM





m = "hello你好"*10
public , private = RSAKG(1024, 65537)
message = bytearray(m.encode('utf8'))
cipher , k = RSA_OAEP_Encrypt(public, message)
recovered = RSA_OAEP_Decrypt(private , cipher , k)
c = recovered.decode('utf8')
print(c)



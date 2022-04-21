# Integer to Octet-String Primitive
def I2OSP(x : int ,l : int) -> bytearray :
    '''
    x : nonnegative integer to be converted
    l : intended length of the resulting octet string
    Output: X corresponding octet string of length l
    Errors: "integer too large"
    '''
    if x > 256 ** l :
        raise Exception("Integer too large")
    res = bytearray()
    while x:
        res.append(x % 256)
        x //= 256
    res += bytearray([0 for i in range(l - len(res))]) # pad with 0
    return res[::-1]
    
# Octet String to Integer Primitive
def OS2IP(X : bytearray) -> int :
    '''
    X : octet string to be converted
    Output: x corresponding nonnegative integer
    '''
    X = X[::-1]
    res = 0
    for i in range(len(X)):
        res += X[i] * 256**i
    return res


# RSA Encryption Primitive
def RSAEP( PublicKey : tuple , m : int ) -> int :
    n,e  = PublicKey
    if m >= n : raise Exception("message larger then public modulo n")
    return pow(m,e,n)

# RSA Decryption Primitive
def RSADP(PrivateKey : tuple , c : int) -> int :
    n,d = PrivateKey
    if c >= n : raise Exception("cipher larger then public modulo n")
    return pow(c,d,n)
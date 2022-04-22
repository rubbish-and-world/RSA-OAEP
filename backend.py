import eel
import RSA_OAEP
import base64
import json

@eel.expose
def KG(L = 1024 , e = 65537):
    ((n,e),(n,d)) = RSA_OAEP.RSAKG( L , e )
    return json.dumps(((str(n),str(e)),(str(n),str(d))))
    """
    JavaScript loses integer accuracy after Number.MAX_SAFE_INTEGER (9,007,199,254,740,991),
    which is obviously smaller than our key, so we have to return it in form of string.
    In JavaScript, use BigInt to hold large numbers
    """


@eel.expose
def Encrypt(E_paraphernalia : str ) -> str :
    d = json.loads(E_paraphernalia)
    message = d['message']
    (n,e) = d['publicKey']
    publicKey = (int(n) , int(e))
    OC,k = RSA_OAEP.RSA_OAEP_Encrypt(publicKey , bytearray(message.encode('utf8')))
    cipher = base64.b64encode(OC).decode('utf8') , k
    return json.dumps(cipher)


@eel.expose
def Decrypt(D_paraphernalia : str ) -> str :
    dic = json.loads(D_paraphernalia)
    cipher = dic['cipher']
    (n,d) = dic['privateKey']
    privateKey = (int(n) , int(d))
    k = dic['k']
    DM = RSA_OAEP.RSA_OAEP_Decrypt(privateKey , bytearray(base64.b64decode(cipher.encode('utf8'))) , k)
    return DM.decode('utf8')





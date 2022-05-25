
async function GenerateKey(){
    //check if key exists
    var element = document.getElementsByClassName("keypair")
    if (element.length > 0){
        for ( var i = 0 ;  i < 2 ; i++){
            //the remove machanism is like queue, after pop, the second become the first
            element[0].remove();
        }
    }
    else{
        //generate key
        keysobj = await eel.KG()();  
        parsedkeys = JSON.parse(keysobj)
        publicKey  = parsedkeys[0]
        privateKey = parsedkeys[1]

        //show keys
        showKeys(parsedkeys)
    }

}

async function encrypt(){

    //get the message
    let message = document.getElementById('message').value

    //get public key
    let publicKey = document.getElementById('userPublicKey').value.split(',')

    //encrypt message with publicKey
    E_paraphernalia = { 'message' : message , 'publicKey' : publicKey }
    cipherobj = await eel.Encrypt(JSON.stringify(E_paraphernalia))();
    [cipher , k] = JSON.parse(cipherobj)

    //show encrypt result and k
    let cipherbox = document.createElement("div");
    cipherbox.innerHTML = "encrypted message : " + cipher + '\n' + "k :" + k
    cipherbox.id = "cipherbox"
    document.body.appendChild(cipherbox)
}


async function decrypt(){
    //get the cipher
    let cipher = document.getElementById('cipher').value

    //get private key
    let privateKey = document.getElementById('userPrivateKey').value.split(',')

    //get k
    let k = parseInt( document.getElementById('k').value )

    //decrypt the cipher with privateKey
    D_paraphernalia = {"cipher" : cipher , "privateKey" : privateKey , "k" : k}
    dcipher = await eel.Decrypt(JSON.stringify(D_paraphernalia))();

    //show decrypt result
    let res = document.createElement('div')
    res.innerHTML = 'decrypted message : '+ '\n' + dcipher
    res.id = "dcipherbox"
    document.body.appendChild(res)
}

function showKeys(keys){
    publicKey  = keys[0]
    privateKey = keys[1]
    showKey('public', publicKey)
    showKey('private', privateKey)
}

function showKey(name, singleKeyPair){
    [n,k] = singleKeyPair
    let keypair = document.createElement('div')
    keypair.innerHTML =  name + ' :' + '\n' + n + ',' + k
    keypair.className = 'keypair'
    document.body.append(keypair)
}


function clearpage(){
    document.getElementById("cipherbox").remove()
    document.getElementById("dcipherbox").remove()
}

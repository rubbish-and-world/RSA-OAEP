async function encrypt(){
    //generate key
    keysobj = await eel.KG()();  
    [publicKey , privateKey] = JSON.parse(keysobj)

    //get the message
    let message = document.getElementById('message').value

    //encrypt message with publicKey
    E_paraphernalia = { 'message' : message , 'publicKey' : publicKey }
    cipherobj = await eel.Encrypt(JSON.stringify(E_paraphernalia))();
    [cipher , k] = JSON.parse(cipherobj)

    //decrypt the cipher with privateKey
    D_paraphernalia = {"cipher" : cipher , "privateKey" : privateKey , "k" : k}
    dcipher = await eel.Decrypt(JSON.stringify(D_paraphernalia))();

    //show result
    let res = document.createElement('div')
    res.innerHTML = 'decrypted message : ' + dcipher
    document.body.appendChild(res)
}

function showKeys(keys){
    [publicKey , privateKey] = keys
    showKey('public', publicKey)
    showKey('private', privateKey)
}

function showKey(name, singleKeyPair){
    [n,k] = singleKeyPair
    let label = document.createElement('div')
    label.innerHTML = name + ' :'
    let modulo = document.createElement('div')
    modulo.innerHTML = 'n : ' + n
    let key = document.createElement('div')
    key.innerHTML = 'k : ' + k
    label.appendChild(modulo)
    label.appendChild(key)
    document.body.appendChild(label)
}

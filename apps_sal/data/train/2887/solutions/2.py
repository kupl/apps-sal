import base64

def adFly_decoder(sc):
    #your code here
    code1 = ''
    code2 = ''
    flg = True
    for ch in sc:
        if flg:
            code1 += ch
        flg = not flg
        
    flg = True
    for ch in sc[::-1]:
        if flg:
            code1 += ch
        flg = not flg
        
    try:
        s = base64.b64decode(code1 + code2).decode('utf-8')
        s = s.split('//adf.ly/go.php?u=')[1]
        return base64.b64decode(s).decode('utf-8')
    except: 
        return 'Invalid'

def adFly_encoder(url):
    s = '96https://adf.ly/go.php?u='
    e_url = base64.b64encode(bytes(url, 'utf-8')).decode('utf-8')
    s += e_url
    b64 = list(base64.b64encode(bytes(s, 'utf-8')).decode('utf-8'))
    
    yummy = ''
    flg = True
    while b64:
        if flg:
            yummy += b64.pop(0)
        else:
            yummy += b64.pop()
        flg = not flg
    
    return yummy

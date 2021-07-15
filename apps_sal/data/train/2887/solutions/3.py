import base64
from random import randint
def adFly_decoder(sc):
    code1 = sc[0:len(sc):2]
    code2 = sc[len(sc):0:-2]
    print(sc)
    if len(code2)-1 >= 8:
        b = base64.b64decode(code1 + code2)
        b = str(b).split('?')
        return str(base64.b64decode(b[1][2:-1]))[2:-1]
    return 'Invalid'
def adFly_encoder(url):
    url_encoded = str(base64.b64encode(url.encode("ascii")))[2:-1]
    url_adfly = str(randint(0, 9)) + str(randint(0,9)) + 'https://adf.ly/go.php?u=' + url_encoded
    b = base64.b64encode(url_adfly.encode("ascii"))
    b = str(b)[2:-1]
    sc1 = b[0:len(b)//2]
    sc2 = b[len(b)//2:][::-1]
    sc = ""
    idx = 0
    for x in range(len(b)):
        if x % 2 == 0:
            sc += sc1[idx]
        else:
            sc += sc2[idx]
            idx+=1
    return sc
        


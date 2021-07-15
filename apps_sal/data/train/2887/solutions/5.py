import base64
import random

PREFIX = 'https://adf.ly/go.php?u='

def adFly_decoder(sc):
    try:
        decoded = base64.b64decode(sc[::2]+sc[1::2][::-1]).decode('utf-8')
        assert decoded[:2].isdigit()
        decoded = decoded[2:]
        assert decoded.startswith(PREFIX)
        return base64.b64decode(decoded[len(PREFIX):]).decode('utf-8')
    except:
        return 'Invalid'
    
    
def adFly_encoder(url):
    adfly_url = f"{random.randint(0,99):02d}{PREFIX}{base64.b64encode(url.encode('utf-8')).decode('utf-8')}"
    adfly_url = base64.b64encode(adfly_url.encode('utf-8')).decode('utf-8')
    half1 = adfly_url[:(len(adfly_url)+1)//2]
    half2 = adfly_url[(len(adfly_url)+1)//2:]
    result = ''
    while half1:
        result += half1[0]
        half1 = half1[1:]
        if half2:
            result += half2[-1]
            half2 = half2[:-1]
    return result


from base64 import b64decode, b64encode
from random import randint


def adFly_decoder(sc):
    return b64decode(b64decode(sc[::2] + sc[::-2])[26:]).decode('utf-8') or 'Invalid'


def adFly_encoder(url):
    url = f'{randint(0, 99):02d}https://adf.ly/go.php?u={url}'.encode('utf-8')
    encoded = b64encode(url[:26] + b64encode(url[26:])).decode('utf-8')
    length = len(encoded) // 2
    return ''.join((x + y for (x, y) in zip(encoded[:length], encoded[:length - 1:-1])))

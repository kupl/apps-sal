import base64
import binascii
import math
from itertools import zip_longest


def adFly_decoder(sc):
    code1 = ""
    code2 = ""
    flip = False
    for c in sc:
        if flip:
            code2 += c
        else:
            code1 += c
        flip = not flip

    try:
        url = base64.b64decode(code1 + code2[len(code2):: -1])
    except binascii.Error:
        return "Invalid"

    try:
        dec = base64.b64decode(url[26:])
    except binascii.Error:
        return "Invalid"

    return str(dec, "utf-8")


def adFly_encoder(url):
    prefix = "96https://adf.ly/go.php?u="
    full = str.encode(prefix) + base64.b64encode(str.encode(url))
    enc = base64.b64encode(full)
    cut = math.ceil(len(enc) / 2)
    code1 = str(enc[: cut + 1], "utf-8")
    code2 = str(enc[len(enc): cut: -1], "utf-8")
    swp = "".join(i + (j or "") for i, j in zip_longest(code1, code2))
    return swp

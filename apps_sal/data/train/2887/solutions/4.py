import random
import base64


def adFly_decoder(sc):
    code1 = ""
    code2 = ""

    for i in range(len(sc)):
        if i % 2 == 0:
            code1 += sc[i]
        else:
            code2 += sc[i]
    code2 = code2[::-1]
    code1 += code2
    try:
        decodeStr = str(base64.b64decode(code1))[2:-1]
    except base64.binascii.Error as err:
        return "Invalid"
    else:
        a = base64.b64decode(decodeStr[decodeStr.find("?u=") + 3:])
        return str(a)[2:-1]


def adFly_encoder(url):
    decodeStr = str(base64.b64encode(bytes(url, encoding="utf-8")))[2:-1]
    ran = random.randint(10, 99)
    modStr = str(base64.b64encode(bytes(str(ran) + "https://adf.ly/go.php?u=" + decodeStr, encoding="utf-8")))[2:-1]
    code1 = modStr[:len(modStr) // 2]
    code2 = modStr[len(modStr) // 2:]
    res = ""
    ic1 = ic2 = 0
    for i in range(len(modStr)):
        if i % 2 == 0:
            res += code1[ic1]
            ic1 += 1
        else:
            res += code2[ic2 - 1]
            ic2 -= 1
    return res

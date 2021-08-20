import base64


def adFly_decoder(sc):
    code1 = ''
    code2 = ''
    for i in range(len(sc)):
        if i % 2 == 0:
            code1 = code1 + sc[i]
        else:
            code2 = code2 + sc[i]
    try:
        url = base64.b64decode((code1 + code2[::-1]).encode())[26:]
        return base64.b64decode(url).decode()
    except:
        return 'Invalid'


def adFly_encoder(url):
    plain = f'00https://adf.ly/go.php?u={base64.b64encode(url.encode()).decode()}'
    code = base64.b64encode(plain.encode()).decode()
    i = len(code) // 2
    (code1, code2) = (code[:i], code[i:][::-1])
    ysmm = ''
    for (ch1, ch2) in zip(code1, code2):
        ysmm = ysmm + ch1 + ch2
    return ysmm

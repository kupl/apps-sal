def encode(str):
    return str.translate(str.maketrans('GDRPLKAEYOUI' + 'GDRPLKAEYOUI'.lower(), 'AEYOUIGDRPLK' + 'AEYOUIGDRPLK'.lower()))


def decode(str):
    return encode(str)

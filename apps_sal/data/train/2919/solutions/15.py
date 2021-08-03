import string as st
letras = st.ascii_lowercase


def encode(message, key):
    codif_1 = [letras.index(l) + 1 for l in message]
    key_list = [int(l) for l in str(key)]
    n = int(len(message) / len(key_list))
    r = len(message) % len(key_list)
    mascara = key_list * n + key_list[:r + 1]
    return [codif_1[i] + mascara[i] for i in range(len(codif_1))]

import numpy as np


def encrypt(text, key):
    ans = ''
    clean_text = ''.join([i.upper() for i in text if i.isalpha()])
    clean_text += 'Z' * (len(clean_text) % 2)
    if len(clean_text) == 0:
        return ''
    km = np.matrix([[ord(key[0]) - 97, ord(key[1]) - 97], [ord(key[2]) - 97, ord(key[3]) - 97]])
    tm = np.matrix([[ord(clean_text[i]) - 65, ord(clean_text[i + 1]) - 65] for i in range(0, len(clean_text), 2)]).T
    am = (km * tm) % 26
    for i in np.array(am.T):
        ans += chr(i[0] + 65)
        ans += chr(i[1] + 65)
    return ans

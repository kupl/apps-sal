ADFGX = ['A', 'D', 'F', 'G', 'X']


def adfgx_encrypt(plaintext_, square):
    plaintext = plaintext_.replace('j', 'i') if 'i' in square else plaintext_.replace('i', 'j')
    return ''.join([ADFGX[square.index(ch) // 5] + ADFGX[square.index(ch) % 5] for ch in plaintext])


def adfgx_decrypt(ciphertext, square):
    return ''.join([square[ADFGX.index(j) + ADFGX.index(i) * 5]
                    for i, j in zip(ciphertext[:-1:2], ciphertext[1::2])])

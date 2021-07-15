ADFGX = 'A','D','F','G','X'

def adfgx_encrypt(plaintext, square):
    ciphertext = ''
    for char in plaintext:
        try: y,x = divmod(square.index(char), 5)
        except ValueError: y,x = divmod(square.index('i'), 5)
        ciphertext += ADFGX[y] + ADFGX[x]
    return ciphertext
    
def adfgx_decrypt(ciphertext, square):
    plaintext = ""
    for j,i in zip(ciphertext[::2], ciphertext[1::2]):
        plaintext += square[ADFGX.index(j)*5+ADFGX.index(i)]
    return plaintext

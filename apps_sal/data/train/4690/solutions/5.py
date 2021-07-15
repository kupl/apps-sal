def adfgx_encrypt(s, square):
    square, s = [e.replace('j', 'i') for e in [square, s]]
    
    E = {v:r+c for row, r in zip([square[i:i+5] for i in range(0, 25, 5)], 'ADFGX') for c, v in zip('ADFGX', row)}
    return ''.join(E[c] for c in s)
    
def adfgx_decrypt(s, square):
    D = {r+c:v for row, r in zip([square[i:i+5] for i in range(0, 25, 5)], 'ADFGX') for c, v in zip('ADFGX', row)}
    return ''.join(D[w] for w in [s[i:i+2] for i in range(0, len(s), 2)])

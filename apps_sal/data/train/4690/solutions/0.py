from itertools import product
import re

KEY = [ a+b for a, b in product("ADFGX", repeat=2) ]
   

def adfgx_encrypt(plaintext, square):
    d      = dict(zip(square, KEY))
    oddity = d['i'] if 'i' in d else d['j']
    return ''.join(d.get(c, oddity) for c in plaintext)
    
    
def adfgx_decrypt(ciphertext, square):
    d      = dict(zip(KEY, square))
    IJkey  = [ k for k, v  in d.items() if v in 'ij'].pop()

    return ''.join( d.get(c, d[IJkey]) for c in re.findall(r'.{2}', ciphertext)) 

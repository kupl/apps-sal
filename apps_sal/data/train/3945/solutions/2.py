import math
def decipher_message(m):
    l = int(math.sqrt(len(m)))  
    return ''.join(''.join(m[i+l*j] for j in range(l)) for i in range(l))

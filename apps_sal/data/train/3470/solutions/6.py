def to_twos_complement(binary, bits):
    binary = binary.replace(" ", "")
    chiffre = binary[0]
    n = int(binary, 2)
    if chiffre == '1':
        n -= 2**bits
    return n
def from_twos_complement(n, bits):
    
    if n<0:
        n += 2**bits
        
    chaine = bin(n)
    chaine = chaine[2:]
    chaine = (bits-len(chaine))*'0'+chaine
    return chaine


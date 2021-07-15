def to_twos_complement(binary, bits):
    x=int(binary.replace(' ',''),2)
    if binary[0]=='0':
        return x
    else:
        return -((x^(2**bits-1))+1)
    

def from_twos_complement(n, bits):
    if n>=0:
        return '{:b}'.format(n).zfill(bits)
    else:
        return '{:b}'.format(2**bits+n).zfill(bits)

def to_twos_complement(binary, bits): 
    conv = int(binary.replace(' ',''), 2)
    return conv - (conv >= 2**bits/2) * 2**bits

def from_twos_complement(n, bits):
    return ("{:0>"+str(bits)+"b}").format(n + (2**bits) * (n<0))

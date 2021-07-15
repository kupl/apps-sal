from math import log2
def switch_endian(n, bits):
    if bits<8 or 2**int(log2(bits))!=bits or 2**bits-1<n:
        return None
    s='{:X}'.format(n).zfill(bits//4)
    r=''
    for i in range(0,len(s),2):
        r=s[i:i+2]+r
    return int(r,16)

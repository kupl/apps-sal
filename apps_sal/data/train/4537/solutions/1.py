def bitlist(func):
    def wrapper(bits):
        i = int(''.join([str(b) for b in bits]), 2)
        result = func(i)
        return [int(b) for b in bin(result)[2:]]
    return wrapper

@bitlist
def bin2gray(bits):
    return bits >> 1 ^ bits

@bitlist
def gray2bin(bits):
    mask = bits >> 1
    while(mask != 0):
         bits ^= mask
         mask >>= 1
    return bits


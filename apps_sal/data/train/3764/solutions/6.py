def arbitrate(b, n):
    return bin(int(2 ** (~-int(b, 2).bit_length())))[2:].zfill(n)

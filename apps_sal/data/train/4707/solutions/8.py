def to_bytes(n):
    return [''.join(t) for t in zip(*[iter(format(n,'0{}b'.format((max(1,n.bit_length())+7)//8*8)))]*8)]

flip_bit=lambda v, i: int("".join([l if 64-i!=k else "0" if l=="1" else "1" for k,l in enumerate(("0"*64+bin(v)[2:])[-64:])]),2)

def hex_hash(s):
    return sum(sum(int(c) for c in hex(ord(c))[2:] if c in "0123456789") for c in s)

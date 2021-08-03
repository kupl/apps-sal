def encode(uncoded):
    encoded = ''.join(''.join(b * 3 for b in bin(ord(c))[2:].zfill(8)) for c in uncoded)
    return encoded


def decode(encoded):
    patches = {'000': '0', '001': '0', '010': '0', '100': '0', '011': '1', '101': '1', '110': '1', '111': '1'}
    patched = ''.join(patches[encoded[i:i + 3]] for i in range(0, len(encoded), 3))
    decoded = ''.join(chr(int(patched[i:i + 8], 2)) for i in range(0, len(patched), 8))
    return decoded

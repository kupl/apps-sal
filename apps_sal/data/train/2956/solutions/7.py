def encode(string):
    bits = ''.join([format(i, '#010b').replace('0b', '') for i in [ord(i) for i in string]])
    return ''.join([i * 3 for i in bits])


def decode(bits):
    parts = [bits[i:i + 3] for i in range(0, len(bits), 3)]
    bits = ''.join(['1' if i.count('1') > i.count('0') else '0' for i in parts])
    return ''.join([chr(int(bits[i:i + 8], 2)) for i in range(0, len(bits), 8)])

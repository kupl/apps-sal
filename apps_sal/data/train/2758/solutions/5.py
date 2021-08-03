def decode(number):
    parts = str(number).rstrip('98').split('98')
    parts[::2] = (''.join(chr(0x60 + int(b + c)) for _, b, c in zip(*[iter(part)] * 3)) for part in parts[::2])
    parts[1::2] = (str(int(part, 2)) for part in parts[1::2])
    return ', '.join(parts)

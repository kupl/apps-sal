import struct

CHARSET = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'
           'abcdefghijklmnopqrstuvwxyz'
           '0123456789!#$%&()*+,./:;<=>?@[]^_`{|}~"')

def b91decode(message):
    value = stack = 0
    out = bytes()
    for first, second in zip(message[::2], message[1::2]):
        cipher = CHARSET.index(first) + CHARSET.index(second) * 91
        value |= cipher << stack
        stack += 13 + ((cipher & 8191) < 89)
        while stack > 7:
            out    += struct.pack('B', value & 255)
            value >>= 8
            stack  -= 8
    if len(message) % 2:
        rogue = message[-1]
        out  += struct.pack('B', (value | CHARSET.index(rogue) << stack) & 255)
    return out.decode('utf-8')

def b91encode(data):
    value = stack = 0
    out = ''
    for (byte,) in struct.iter_unpack('B', bytes(data, 'utf-8')):
        value |= byte << stack
        stack += 8
        if stack > 13:
            cipher = value & 8191
            if cipher > 88:
                value >>= 13
                stack  -= 13
            else:
                cipher  = value & 16383
                value >>= 14
                stack  -= 14
            out += CHARSET[cipher % 91] + CHARSET[cipher // 91]
    return out + (value > 0) * CHARSET[value % 91]

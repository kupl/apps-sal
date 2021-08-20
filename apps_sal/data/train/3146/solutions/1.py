def to_utf8_binary(string):
    return ''.join(('{:08b}'.format(b) for b in string.encode('utf8')))


def from_utf8_binary(bitstring):
    import re
    return bytes((int(b, 2) for b in re.split('(........)', bitstring) if b)).decode('utf-8')

from textwrap import wrap

def to_utf8_binary(string):
    return ''.join(format(x, 'b').rjust(8, '0') for x in bytearray(string, 'utf-8'))
 
def from_utf8_binary(bitstring):
    return bytearray([int(t, 2) for t in wrap(bitstring, 8)]).decode()


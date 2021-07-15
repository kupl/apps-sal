def to_utf8_binary(string):
    bitstring = ''
    for char in string:
        code = ord(char)
        if code < 128:
            bitstring += ('0000000000' + bin(code)[2:])[-8:]
        elif code < 2048:
            binary = ('0' * 12 + bin(code)[2:])[-11:]
            bitstring += '110' + binary[0:5] + '10' + binary[5:11]
        elif code < 65536:
            binary = ('0' * 16 + bin(code)[2:])[-16:]
            bitstring += '1110' + binary[0:4] + '10' + binary[4:10] + '10' + binary[10:16]
        else:
            binary = ('0' * 21 + bin(code)[2:])[-21:]
            bitstring += '11110' + binary[0:3] + '10' + binary[3:9] + '10' + binary[9:15] + '10' + binary[15:21]
    return bitstring

def from_utf8_binary(bitstring):
    string = ''
    i, t = 0, len(bitstring)
    while i < t:
        bit_code = ''
        char_bit = bitstring[i:i+8]
        i += 8
        
        if char_bit.startswith('11110'):
            bit_code += char_bit[5:8]
            for j in range(0, 3):
                char_bit = bitstring[i:i+8]
                bit_code += char_bit[2:8]
                i += 8
        elif char_bit.startswith('1110'):
            bit_code += char_bit[4:8]
            for j in range(0, 2):
                char_bit = bitstring[i:i+8]
                bit_code += char_bit[2:8]
                i += 8
        elif char_bit.startswith('110'):
            bit_code += char_bit[3:8]
            for j in range(0, 1):
                char_bit = bitstring[i:i+8]
                bit_code += char_bit[2:8]
                i += 8
        else:
            bit_code = '0' + char_bit[1:8]
        
        string += chr(int(bit_code, 2))
            
    return string

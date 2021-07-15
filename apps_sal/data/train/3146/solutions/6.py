def utf8_char_to_binary(ch):
    string = str(bin( ord(ch) ))[2:]
    if len(string) <= 7: return '0' + string.rjust(7, '0')
    result, bts = [], 1
    while len(string) + (bts+1) > 8:
        bts += 1
        result.insert(0, "10" + string[-6:].rjust(6, '0'))
        string = string[:-6]
    return "".join(['1'*bts + '0' + string.rjust(8-bts-1, '0')] + result)
        
def to_utf8_binary(string):
    return "".join( map(utf8_char_to_binary, list(string)) )

def bitstring_to_utf8_chr(bitstring):
    if len(bitstring) == 0:
        return ''
    if len(bitstring) == 8:
        return chr(int(bitstring, 2))
    else:
        binary = ""
        byte_parts = [bitstring[i:i+8] for i in range(0, len(bitstring), 8)]
        binary += byte_parts[0][list(byte_parts[0]).index('0'):]
        for i in range(1, len(byte_parts)):
            binary += byte_parts[i][2:]
        return chr(int(binary, 2))

def from_utf8_binary(bitstring):
    bitstring = [bitstring[i:i+8] for i in range(0, len(bitstring), 8)]
    character_bitstring, final_string = '', ''
    for s in bitstring:
        if s[:2] == '10':
            character_bitstring += s
        elif s[0] == '0':
            final_string += (bitstring_to_utf8_chr(character_bitstring) + bitstring_to_utf8_chr(s))
            character_bitstring = ""
        else:
            final_string += bitstring_to_utf8_chr(character_bitstring)
            character_bitstring = s
    return final_string + bitstring_to_utf8_chr(character_bitstring)


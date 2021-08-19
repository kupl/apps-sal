def decodeBits(bits):
    bits = bits.strip('0')
    time_unit = min(list(map(len, bits.replace('1', ' ').split() + bits.replace('0', ' ').split())))
    word_sep = '0' * 7 * time_unit
    char_sep = '0' * 3 * time_unit
    ones_sep = '0' * 1 * time_unit
    dash = '1' * 3 * time_unit
    dot = '1' * 1 * time_unit
    return bits.replace(dash, '-').replace(dot, '.').replace(word_sep, '   ').replace(char_sep, ' ').replace(ones_sep, '')


def decodeMorse(morse_code):
    return ' '.join((''.join(map(MORSE_CODE.get, word.split())) for word in morse_code.split('   '))).strip()

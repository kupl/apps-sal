def decodeBits(bits):
    unit = min([len(item) for item in bits.strip('0').split('0') if len(item) != 0] + [len(item) for item in bits.strip('0').split('1') if len(item) != 0])
    return bits.replace('111' * unit, '-').replace('0000000' * unit, '  ').replace('000' * unit, ' ').replace('1' * unit, '.').replace('0', '')


def decodeMorse(morseCode):
    return ''.join([MORSE_CODE.get(letter, ' ') for letter in morseCode.strip().split(' ')])

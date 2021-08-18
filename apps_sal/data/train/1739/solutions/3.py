from re import split


def decodeBits(bits):
    unit = min([len(s) for s in split(r'0+', bits.strip('0'))] + [len(s) for s in split(r'1+', bits.strip('0')) if s != ''])
    return bits.replace('0' * unit * 7, '   ').replace('0' * unit * 3, ' ').replace('1' * unit * 3, '-').replace('1' * unit, '.').replace('0', '')


def decodeMorse(morseCode):
    return ' '.join(''.join(MORSE_CODE[letter] for letter in word.split(' ')) for word in morseCode.strip().split('   '))

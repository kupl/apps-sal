MORSE_CODE['_'] = ' '


def decodeBits(bits):
    bits = bits.strip('0')

    if '0' not in bits:
        return '.'

    minOnes = min(len(s) for s in bits.split('0') if s)
    minZeros = min(len(s) for s in bits.split('1') if s)
    m = min(minOnes, minZeros)

    return bits.replace('111' * m, '-').replace('0000000' * m, ' _ ').replace('000' * m, ' ').replace('1' * m, '.').replace('0' * m, '')


def decodeMorse(morseCode):
    return ''.join(MORSE_CODE[c] for c in morseCode.split())

def decodeBits(bits):
    bits = bits.strip('0')
    if '0' not in bits:
        return '.'
    u = 1
    while '0' * u not in bits.split('1') and '1' * u not in bits.split('0'):
        u += 1
    return ' '.join([char.replace('1' * 3 * u, '-').replace('1' * u, '.').replace('0', '') for char in bits.split('0' * 3 * u)])


def decodeMorse(morseCode):
    MORSE_CODE[''] = ' '
    arr = [MORSE_CODE[x] for x in morseCode.strip().split(' ')]
    return ''.join(arr).replace('  ', ' ')

def decodeBits(bits):
    import re

    # remove trailing and leading 0's
    bits = bits.strip('0')

    # find the least amount of occurrences of either a 0 or 1, and that is the time hop
    time_unit = min(len(m) for m in re.findall(r'1+|0+', bits))

    # hop through the bits and translate to morse
    return bits[::time_unit].replace('111', '-').replace('1', '.').replace('0000000', '   ').replace('000', ' ').replace('0', '')


def decodeMorse(morseCode):
    return ' '.join(''.join(MORSE_CODE[l] for l in w.split()) for w in morseCode.split('   '))

def decodeBits(bits):
    mcode = {-1: '', -3: ' ', -7: '   ', 1: '.', 3: '-'}
    (m, b) = ([], '')
    for bit in bits.strip('0'):
        if bit == b:
            m[-1] += 1 if bit == '1' else -1
        else:
            m.append(1 if bit == '1' else -1)
        b = bit
    timeunit = min([abs(bb) for bb in m])
    return ''.join([mcode[bb / timeunit] for bb in m])


def decodeMorse(morseCode):
    return ' '.join((''.join((MORSE_CODE[c] for c in w.split())) for w in morseCode.strip().split('   ')))

from re import compile

TOKENIZER = compile('(0+)')


def decodeBits(bits):
    tokens = TOKENIZER.split(bits.strip('0'))
    lenDot = min(len(token) for token in tokens)
    lenDash = 3 * lenDot
    ret = []
    for token in tokens:
        if token[0] == '1':
            ret.append('.' if len(token) < lenDash else '-')
        elif len(token) > lenDot:
            ret.append(' ' if len(token) <= lenDash else '   ')
    return ''.join(ret)


def decodeMorse(morseCode):
    return ' '.join(''.join(MORSE_CODE[c] for c in word.split(' ')) for word in morseCode.strip().split('   '))

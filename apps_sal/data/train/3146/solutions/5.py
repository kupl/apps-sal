def to_utf8_binary(string):

    stList = list(string)
    bincodes = [toBin(c) for c in stList]
    return ''.join(bincodes)


def toBin(string):
    print((ord(string)))
    a = bin(ord(string))[2:]
    if(ord(string) <= 127):
        padded = a.zfill(8)
        return (padded)
    elif ord(string) <= 2047:
        padded = a.zfill(11)
        return '110' + padded[:5] + '10' + padded[5:]
    elif ord(string) <= 65535:
        padded = a.zfill(16)
        part1 = '1110' + padded[:4]
        remaining = padded[4:]
        part2 = '10' + remaining[:6]
        remaining = remaining[6:]
        part3 = '10' + remaining
        return part1 + part2 + part3
    elif ord(string) <= 1114111:
        print(a)
        padded = a.zfill(21)
        part1 = '11110' + padded[:3]
        print(part1)
        remaining = padded[3:]
        part2 = '10' + remaining[:6]
        print(part2)
        remaining = remaining[6:]
        part3 = '10' + remaining[:6]
        remaining = remaining[6:]
        part4 = '10' + remaining[:6]
        return part1 + part2 + part3 + part4


def splitEveryN(n, li):
    return [li[i:i + n] for i in range(0, len(li), n)]


def getLenInByte(part):
    print(part)
    if part[0] == '0':
        return 1
    elif part[:3] == '110':
        print('two bytes')
        return 2
    elif part[:4] == '1110':
        return 3
    elif part[:5] == '11110':
        return 4


def from_utf8_binary(bitstring):
    li = splitEveryN(8, bitstring)
    i = 0
    result = []
    while(i < len(li)):
        bytelen = getLenInByte(li[i])
        nextbin = li[i: i + bytelen]
        joined = ''.join(nextbin)

        frombin = fromBin(joined)
        result += frombin
        i += bytelen
    return ''.join(result)


def fromBin(bitstring):
    if len(bitstring) <= 8:
        return chr(int(bitstring, 2))
    elif len(bitstring) <= 16:
        part1 = bitstring[3:8]
        part2 = bitstring[10:16]
        bi = part1 + part2
        return chr(int(bi, 2))
    elif len(bitstring) <= 24:
        part1 = bitstring[4:8]
        part2 = bitstring[10:16]
        part3 = bitstring[18:]
        return chr(int(part1 + part2 + part3, 2))
    elif len(bitstring) <= 32:
        part1 = bitstring[5:8]
        part2 = bitstring[10:16]
        part3 = bitstring[18:24]
        part4 = bitstring[26:]
        return chr(int(part1 + part2 + part3 + part4, 2))
    return ''

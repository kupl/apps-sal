from re import compile
REGEX1 = compile('0+|1+').findall
REGEX2 = compile('(0+) (0+)').findall
binary = '{:07b}'.format


def send(s):
    temp = ''.join((binary(ord(c)) for c in s))
    return ' '.join(('0 ' + '0' * len(x) if x[0] == '1' else '00 ' + x for x in REGEX1(temp)))


def receive(s):
    temp = ''.join((y if x == '00' else '1' * len(y) for (x, y) in REGEX2(s)))
    return ''.join((chr(int(temp[i:i + 7], 2)) for i in range(0, len(temp), 7)))

import re


def send(s):
    return ' '.join(('0' * (2 - int(c[0])) + ' ' + '0' * len(c) for c in re.findall('1+|0+', ''.join((f'{ord(c):07b}' for c in s)))))


def receive(s):
    return ''.join((chr(int(''.join(a), 2)) for a in zip(*[iter(''.join((str(2 - len(a)) * len(b) for (a, b) in zip(*[iter(s.split())] * 2))))] * 7)))

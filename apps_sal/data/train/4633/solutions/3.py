def convert(number):
    return ''.join((chr(int(f'{e1}{e2}')) for (e1, e2) in zip(*[iter(number)] * 2)))

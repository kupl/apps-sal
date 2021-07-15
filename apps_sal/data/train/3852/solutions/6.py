def ips_between(start, end):
    n1 = int(''.join(f'{n:08b}' for n in map(int, start.split('.'))), 2)
    n2 = int(''.join(f'{n:08b}' for n in map(int, end.split('.'))), 2)
    return n2 - n1

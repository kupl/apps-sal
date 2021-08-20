t = int(input())


def conv(n):
    k = bin(n)
    k = k[2:]
    z = len(k)
    c = '1' * z
    if c == k:
        return False


def find(n):
    x = bin(n)[2:]
    str = ''
    for i in x[::-1]:
        if i == '0':
            str += '1'
            break
        else:
            str += '0'
    return int(str[::-1], 2)


for i in range(t):
    n = int(input())

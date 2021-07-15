n = int(input())

d = {}

def get_mask(num):
    res = ''
    for el in num:
        if (int(el) & 1):
            res += '1'
        else:
            res += '0'

    return '0' * (18 - len(num)) + res
    

for _ in range(n):
    c, v = input().split(' ')
    if c == '?':
        v = '0' * (18 - len(v)) + v
        if v in d.keys():
            print(d[v])
        else:
            print(0)
    elif c == '+':
        v = get_mask(v)
        if v in d.keys():
            d[v] += 1
        else:
            d[v] = 1
    else:
        v = get_mask(v)
        d[v] -= 1

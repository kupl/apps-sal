str1 = int(input())
for i in range(str1):
    l1 = []
    str2 = input()
    for i in str2:
        l1.append(i)
    count = 0
    d = dict()
    d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14}
    d1 = {'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    d.update(d1)
    for j in l1:
        if j not in ['a', 'e', 'i', 'o', 'u']:
            a = abs(d[j] - d['a'])
            e = abs(d[j] - d['e'])
            i = abs(d[j] - d['i'])
            o = abs(d[j] - d['o'])
            u = abs(d[j] - d['u'])
            count += min([a, e, i, o, u])
    print(count)

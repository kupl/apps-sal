from itertools import permutations
for j in range(int(input())):
    n = input()
    c = ''
    x = list(permutations(n, 2))
    a = set(x)
    for i in a:
        z = i[0] + i[1]
        if int(z) >= 65 and int(z) <= 90:
            c += chr(int(z))
    if c == '':
        print('')
    else:
        am = list(c)
        am.sort()
        bm = ''.join(am)
        print(bm)

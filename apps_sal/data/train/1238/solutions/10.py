from collections import Counter
for i in range(int(input())):
    a = [int(i) for i in str(input())]
    a1 = []
    asdf = Counter(a)
    for n in range(65, 91):
        nn = n % 10
        nn1 = n // 10
        if nn == nn1:
            if asdf[nn] >= 2:
                a1.append(chr(n))
        else:
            if asdf[nn] > 0 and asdf[nn1] > 0:
                a1.append(chr(n))
    print() if len(a1) == 0 else print(''.join(a1))

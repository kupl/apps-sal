from itertools import permutations
from collections import Counter
for _ in range(int(input())):
    a = list(input())
    a = map(int, a)
    z = dict(Counter(a))
    l = list(z.keys())
    for i in sorted(z.keys()):
        j = z[i]
        if i > 5:
            if j > 1:
                for k in sorted(l):
                    if i * 10 + k < 91 and i * 10 + k > 64:
                        print(chr(i * 10 + k), end="")
            else:
                l.remove(i)
                for k in sorted(l):
                    if i * 10 + k < 91 and i * 10 + k > 64:
                        print(chr(i * 10 + k), end="")
                l.append(i)
    print()

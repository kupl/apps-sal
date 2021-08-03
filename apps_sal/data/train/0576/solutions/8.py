from math import factorial as fact
from itertools import combinations
for _ in range(int(input())):
    a = input()
    if "a" not in a:
        print(0)
        continue
    ct = a.count("a")
    ct = "a" * ct
    a = a.replace("a", "")
    count = 0
    for i in range(1, len(a) + 1):
        count += (fact(len(a)) / (fact(i) * (fact(len(a) - i))))
    ctcount = 0
    for i in range(1, len(ct) + 1):
        ctcount += len(list(combinations(ct, i)))
    print(int(count) * ctcount + ctcount)

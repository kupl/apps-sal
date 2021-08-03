from collections import Counter
for _ in range(int(input())):
    a = input()
    b = input()
    a1 = Counter(a)
    b1 = Counter(b)
    c = a1 & b1
    if len(c) == 0:
        print(0)
    else:
        d = list(c.elements())
        print(len(d))

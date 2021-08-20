from collections import Counter
t = int(input())
for _ in range(t):
    q = int(input())
    orig_set = set()
    orig_set.add(0)
    (E, O) = (0, 0)
    for row in range(q):
        x = int(input())
        if x in orig_set:
            print(E, O)
        else:
            l = []
            for i in orig_set:
                elem = i ^ x
                if Counter(bin(elem)[2:])['1'] % 2 == 1:
                    O += 1
                else:
                    E += 1
                l.append(elem)
            for e in l:
                orig_set.add(e)
            print(E, O)

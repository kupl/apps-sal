from collections import Counter
t = int(input())
for _ in range(t):
    q = int(input())
    orig_set = set()
    for row in range(q):
        (E, O) = (0, 0)
        x = int(input())
        for i in set(orig_set):
            if i != x:
                orig_set.add(i ^ x)
        orig_set.add(x)
        for elem in orig_set:
            if Counter(bin(elem)[2:])['1'] % 2:
                O += 1
            else:
                E += 1
        print(E, O)

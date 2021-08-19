from itertools import permutations
t = int(input())
for i in range(t):
    n = int(input())
    s = list(str(n))
    l = []
    perm = permutations(s, 2)
    perm = set(list(perm))
    # print(list(perm))
    for i in list(perm):
        # print(i)
        s = ""
        s += str(i[0])
        s += str(i[1])
        s = int(s)
        if(s >= 65 and s <= 90):
            l.append(chr(s))
    l.sort()
    for i in l:
        print(i, end="")

    print()

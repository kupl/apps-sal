from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    s = [int(i) for i in input().split()]
    w = defaultdict(list)
    for i in range(n):
        w[s[i]].append(i)
    typ = len(w)
    keys = sorted(list(w.keys()))
    length = len(keys)
    ele_count = 1
    i = 1
    rnd = 0
    val = keys[0]
    pos = w[keys[0]][0]
    while ele_count < typ:
        if w[keys[ele_count]][-1] < pos:
            rnd+=1
            pos = w[keys[ele_count]][0]
        else:
            i = 0
            while i < len(w[keys[ele_count]]) and w[keys[ele_count]][i]<=pos:
                i+=1
            pos = w[keys[ele_count]][i]
        ele_count+=1
    print(rnd+1)


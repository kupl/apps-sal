import itertools
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    p = [i for i in range(1, n + 1)]
    good = 0
    for i in a:
        if(i != 0):
            p.remove(i)

    x = list(itertools.permutations(p))
    for i in x:
        j = 0
        b = [l for l in a]
        for z in range(n):
            if(b[z] == 0):
                b[z] = i[j]
                j += 1
        loc_cnt = 0
        for z in range(1, n):
            if(b[z] > b[z - 1]):
                loc_cnt += 1
        if(loc_cnt == k):
            good += 1

    print(good)

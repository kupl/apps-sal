import itertools
t = int(input())
for _ in range(t):
    (n, kkk) = list(map(int, input().split()))
    it = list(map(int, input().split()))
    kk = set(list(range(1, n + 1)))
    s = set([i for i in it if i != 0])
    left = kk - s
    mm = list(itertools.permutations(list(left)))
    tot = 0
    for perm in mm:
        k = 0
        mt = it[:]
        ind = 0
        for (j, i) in enumerate(it):
            if i == 0:
                mt[j] = perm[ind]
                ind += 1
            if j > 0:
                if mt[j] > mt[j - 1]:
                    k += 1
        if kkk == k:
            tot += 1
    print(tot)

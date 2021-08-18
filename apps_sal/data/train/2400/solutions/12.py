for tc in range(int(input())):
    n = int(input())
    ls = list(map(int, input().split()))
    if len(set(ls)) == 1:
        print(1)
        print(' '.join(['1' for _ in range(n)]))
    else:
        solo = True
        ngroups = 0
        for i in range(n):
            if ls[i] == ls[i - 1]:
                solo = False
            else:
                ngroups += 1

        shuffle = 1 if (ngroups % 2 and not solo) else 0

        i = 0
        while ls[i] == ls[i - 1]:
            i += 1
        res = [None for _ in range(n)]
        st = 1
        for j in range(n):
            if shuffle and ls[i] == ls[i - 1]:
                st = 3 - st
                shuffle = 0
            res[i] = st
            i = (i + 1) % n
            if ls[i] != ls[i - 1]:
                st = 3 - st

        if st == 2:
            i = (i - 1) % n
            res[i] = 3
            while ls[(i - 1) % n] == ls[i]:
                i = (i - 1) % n
                res[i] = 3

        print(max(res))
        print(' '.join(map(str, res)))

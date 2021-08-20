def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        ar = list(map(int, input().split()))
        if n > 62:
            print('NO')
            continue
        lk = set()
        ok = True
        for sz in range(1, n + 1):
            idx = 0
            while idx + sz - 1 < n:
                curr = 0
                for j in range(idx, idx + sz):
                    curr = curr | ar[j]
                if curr in lk:
                    ok = False
                    break
                else:
                    lk.add(curr)
                idx += 1
        if ok:
            print('YES')
        else:
            print('NO')


def __starting_point():
    main()


__starting_point()

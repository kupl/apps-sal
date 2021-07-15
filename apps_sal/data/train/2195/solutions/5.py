from collections import Counter


def main():
    input()
    cnt = Counter(list(map(int, input().split())))
    a, *rest = sorted(cnt.keys())
    pool, res = cnt[a], 0
    for a in rest:
        c = cnt[a]
        if pool < c:
            res += pool
            pool = c
        else:
            res += c
    print(res)


def __starting_point():
    main()

__starting_point()

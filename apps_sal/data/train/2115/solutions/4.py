def main():
    from collections import Counter
    n, d = list(map(int, input().split()))
    l, cnt, j = list(map(int, input().split())), Counter(), 0
    for i, hi in enumerate(l):
        hi -= d
        while l[j] < hi:
            j += 1
        cnt[i - j] += 1
    print(sum(k * (k - 1) * v for k, v in list(cnt.items())) // 2)


def __starting_point():
    main()

__starting_point()

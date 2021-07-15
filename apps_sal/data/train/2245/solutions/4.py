def main():
    n, m, k = list(map(int, input().split()))
    aa = list(map(int, input().split()))
    lrd = list(tuple(map(int, input().split())) for _ in range(m))
    cnt = [0] * (m + 1)
    for _ in range(k):
        x, y = list(map(int, input().split()))
        cnt[x - 1] += 1
        cnt[y] -= 1
    delta, c = [0] * (n + 1), 0
    for (l, r, d), dc in zip(lrd, cnt):
        c += dc
        d *= c
        delta[l - 1] += d
        delta[r] -= d
    da = 0
    for i, a, d in zip(list(range(n)), aa, delta):
        da += d
        aa[i] = a + da
    print(" ".join(map(str, aa)))


def __starting_point():
    main()

__starting_point()

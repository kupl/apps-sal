def main():
    import sys
    from array import array
    input = sys.stdin.readline

    class Bit:
        def __init__(self, n):
            self.size = n
            self.size_bit_length = n.bit_length()
            self.tree = array('h', [0] * (n + 1))

        def reset(self):
            self.tree = array('h', [0] * (self.size + 1))

        def sum(self, i):
            s = 0
            while i > 0:
                s += self.tree[i]
                i -= i & -i
            return s

        def add(self, i, x):
            while i <= self.size:
                self.tree[i] += x
                i += i & -i

        def lower_bound(self, w):
            if w <= 0:
                return 0
            x = 0
            k = 1 << (self.size_bit_length - 1)
            while k:
                if x + k <= self.size and self.tree[x + k] < w:
                    w -= self.tree[x + k]
                    x += k
                k >>= 1
            return x + 1

    N, M = list(map(int, input().split()))
    dist = [0] + list(map(int, input().split()))
    for i in range(N - 1):
        dist[i + 1] += dist[i]
    B = [0] * (M * N)
    for i in range(N):
        BB = list(map(int, input().split()))
        for j in range(M):
            B[j * N + i] = BB[j] * (N + 1) + i + 1

    imos = []
    for i in range(N + 1):
        imos.append([0] * (N + 1 - i))
    bit = Bit(N)
    for m in range(M):
        bit.reset()
        for bi in sorted(B[m * N: (m + 1) * N], reverse=True):
            b, i = divmod(bi, N + 1)
            k = bit.sum(i)
            l = bit.lower_bound(k)
            r = bit.lower_bound(k + 1)
            imos[l + 1][i - (l + 1)] += b
            if i != N:
                imos[i + 1][0] -= b
            if r != N + 1:
                imos[l + 1][r - (l + 1)] -= b
            if i != N and r != N + 1:
                imos[i + 1][r - (i + 1)] += b
            bit.add(i, 1)

    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            imos[i][j - i] += imos[i][j - 1 - i]
    for i in range(2, N + 1):
        for j in range(i, N + 1):
            imos[i][j - i] += imos[i - 1][j - (i - 1)]
    ans = 0
    for i in range(1, N + 1):
        for j in range(i, N + 1):
            ans = max(ans, imos[i][j - i] - (dist[j - 1] - dist[i - 1]))
    print(ans)


def __starting_point():
    main()


__starting_point()

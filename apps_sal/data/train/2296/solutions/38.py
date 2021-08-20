def main():
    from collections import deque

    class BIT:

        def __init__(self, n):
            self.n = n
            self.maxbit = 2 ** (len(bin(n)) - 3)
            self.bit = [0] * (n + 1)
            self.allsum = 0

        def make_bit(self, a):
            (n, bit) = (self.n, self.bit)
            for (i, j) in enumerate(a):
                x = i + 1
                self.allsum += j
                while x < n + 1:
                    bit[x] += j
                    x += x & -x

        def add(self, i, v):
            (x, n, bit) = (i + 1, self.n, self.bit)
            self.allsum += v
            while x < n + 1:
                bit[x] += v
                x += x & -x

        def sum(self, i):
            (ret, x, bit) = (0, i, self.bit)
            while x > 0:
                ret += bit[x]
                x -= x & -x
            return ret

        def sum_range(self, i, j):
            return self.sum(j) - self.sum(i)

        def lowerbound(self, w):
            if w <= 0:
                return 0
            (x, k, n, bit) = (0, self.maxbit, self.n, self.bit)
            while k:
                if x + k <= n and bit[x + k] < w:
                    w -= bit[x + k]
                    x += k
                k //= 2
            return x
    s = input()
    n = len(s)
    (alpha, center) = ('abcdefghijklmnopqrstuvwxyz', '')
    (counter, must, deque_dict) = (dict(), dict(), dict())
    for c in alpha:
        counter[c] = 0
        deque_dict[c] = deque([])
    for c in s:
        counter[c] += 1
    for (i, j) in list(counter.items()):
        must[i] = j // 2
    if n % 2 == 1:
        for (i, j) in list(counter.items()):
            if j % 2 == 1:
                if center != '':
                    print(-1)
                    return 0
                else:
                    center = i
    else:
        for (i, j) in list(counter.items()):
            if j % 2 == 1:
                print(-1)
                return 0
    half = []
    cnt = 0
    for c in s:
        if must[c] > 0:
            must[c] -= 1
            half.append(c)
            cnt += 1
        if cnt == n // 2:
            break
    half2 = half[::-1]
    if center != '':
        half.append(center)
    s2 = half + half2
    for i in range(n):
        deque_dict[s[i]].append(i)
    ans = 0
    s3 = []
    for c in s2:
        d = deque_dict[c].popleft()
        s3.append(d)
    bit = BIT(n)
    for i in s3:
        ans += bit.sum_range(i, n)
        bit.add(i, 1)
    print(ans)


main()

def solve(n):

    def length(n):
        s = 0
        for i in range(20):
            o = 10 ** i - 1
            if o > n:
                break
            s += (n - o) * (n - o + 1) // 2
        return s

    def binary_search(k):
        n = 0
        for p in range(63, -1, -1):
            if length(n + 2 ** p) < k:
                n += 2 ** p
        return n

    def sequence(n):
        if n < 10:
            return n
        for i in range(1, 19):
            segment = i * 9 * 10 ** (i - 1)
            if n <= segment:
                return str(10 ** (i - 1) + (n - 1) // i)[(n - 1) % i]
            else:
                n -= segment
    return int(sequence(n - length(binary_search(n))))

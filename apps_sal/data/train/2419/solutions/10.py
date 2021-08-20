class Solution:

    def repeatedStringMatch(self, text, pattern):
        (n, m) = (len(text), len(pattern))
        (base, prime) = (256, 257)
        bpow = base ** (m - 1) % prime

        def check(i):
            for j in range(m):
                if text[(i + j) % n] != pattern[j]:
                    return False
            return True

        def compute_hash(s):
            (n, h) = (len(s), 0)
            for i in range(m):
                c = s[i % n]
                h = (h * base + ord(c)) % prime
            return h

        def update_hash(h, old, new):
            dh = ord(old) * bpow % prime
            h = (h - dh + prime) % prime
            h = (h * base + ord(new)) % prime
            return h
        p = compute_hash(pattern)
        t = compute_hash(text)
        for i in range(n):
            if t == p and check(i):
                return 1 + (i + m - 1) // n
            t = update_hash(t, text[i], text[(i + m) % n])
        return -1

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        def generate(n):
            res = [0]
            cur = 1
            while n:
                if n & 1 == 1:
                    res += [i + cur for i in res]
                n >>= 1
                cur <<= 1
            return set(res)

        def to_bit(w):
            res = 0
            for c in w:
                res |= 1 << (ord(c) - ord('a'))
            return res
        m = collections.defaultdict(dict)
        for w in words:
            visited = set()
            for c in w:
                if c in visited:
                    continue
                visited.add(c)
                b = to_bit(w)
                if b not in m[c]:
                    m[c][b] = 1
                else:
                    m[c][b] += 1
        res = []
        for w in puzzles:
            s1, count = m[w[0]], 0
            for i in generate(to_bit(w)):
                if i in s1:
                    count += s1[i]
            res.append(count)

        return res

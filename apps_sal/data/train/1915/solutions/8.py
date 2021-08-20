class Solution:

    def movesToStamp(self, stamp: str, target: str) -> List[int]:

        def check(i):
            found = False
            for j in range(len(s)):
                if t[i + j] == '*':
                    continue
                if t[i + j] != s[j]:
                    return False
                found = True
            if found:
                t[i:i + len(s)] = ['*'] * len(s)
                res.append(i)
            return found
        (n, m, t, s, res) = (len(target), len(stamp), list(target), list(stamp), [])
        while True:
            found = False
            for i in range(n - m + 1):
                found = found or check(i)
            if not found:
                break
        return res[::-1] if t == ['*'] * n else []

class Solution:
    def splitIntoFibonacci(self, s: str) -> List[int]:
        def isTrue(a, b, s):
            if len(str(a) + str(b) + s) != self.n:
                return []
            l = [a, b]
            while True:
                c = str(a + b)
                if int(c) > 2147483647:
                    return []
                l.append(int(c))
                if c == s[:len(c)]:
                    a = b
                    b = int(c)
                    s = s[len(c):]
                    if s == '':
                        return l
                else:
                    return []
        self.n = len(s)
        for i in range(1, len(s)):
            for j in range(i):
                l = isTrue(int(s[0:j + 1]), int(s[j + 1:i + 1]), s[i + 1:])
                if l:
                    return l
        return []

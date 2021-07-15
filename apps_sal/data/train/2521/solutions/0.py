class Solution:
    def reformat(self, s: str) -> str:
        n = [str(i) for i in range(0, 10)]
        a, b = [], []
        for i in s:
            if i in n:
                b.append(i)
            else:
                a.append(i)
        if abs(len(a) - len(b)) > 1:
            return ''
        r = ''
        if len(a) == len(b):
            while a:
                r += a.pop()
                r += b.pop()
        elif len(a) > len(b):
            while b:
                r += a.pop()
                r += b.pop()
            r += a[0]
        else:
            while a:
                r += b.pop()
                r += a.pop()
            r += b[0]
        return r

class Solution:
    def sortString(self, s: str) -> str:
        c = collections.Counter(''.join(sorted(s)))
        a = ''
        while c:
            stack = []
            for i in c.keys():
                if c[i] > 0:
                    a = a+i[0]
                    c[i] -= 1
                if c[i] > 0:
                    stack.append(i)
            while stack:
                j = stack.pop()
                a = a+j[0]
                c[j] -= 1
            c += Counter() # erases all counts of 0
        return a

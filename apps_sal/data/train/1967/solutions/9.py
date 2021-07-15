class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        def f(l, i, leng):
            if leng == len(S) and len(l) >= 3:
                return l
            r = []
            t = 0
            for j in range(i, len(S)):
                t *= 10
                t += int(S[j])
                leng += 1
                if t <= 2**31 - 1:
                    if len(l) > 1 and l[-1] + l[-2] != t:
                        continue
                    l.append(t)
                    temp = f(l, j + 1, leng)
                    if temp:
                        return temp
                    l.pop()
                    if t == 0:
                        return []
            print(r)
            return r
        return f([], 0, 0)       

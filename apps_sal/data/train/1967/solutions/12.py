class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        exp = 2**31 - 1
        def works(x,y,i):
            res = [x,y]
            while i < len(S):
                target = res[-2] + res[-1]
                if target > exp:
                    return []
                build = S[i]
                i += 1
                while i < len(S) and build < target:
                    if build == 0:
                        return []
                    build = build*10 + S[i]
                    i += 1
                if build != target:
                    return []
                res.append(build)
            return res
        S = [int(c) for c in S]
        N = len(S)
        x = 0
        for i in range(N-2):
            if i > 0 and x == 0:
                break
            x = x*10 + S[i]
            y = 0
            for j in range(i+1, N-1):
                if j > i+1 and y == 0:
                    break
                y = y*10 + S[j]
                res = works(x,y,j+1)
                if res: return res
            
        return []

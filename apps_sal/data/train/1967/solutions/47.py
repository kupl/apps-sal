class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        n = len(S)
        for i in range(n):
            fs = S[:i+1]
            if fs != \"0\" and fs.startswith(\"0\"):
                continue
            for j in range(i+1, n):
                ss = S[i+1:j+1]
                if ss != \"0\" and ss.startswith(\"0\"):
                    break
                a, b = int(fs), int(ss)
                fibs = [a, b]
                k = j + 1
                while k < n:
                    next_s = str(fibs[-1] + fibs[-2])
                    next_val = int(next_s)
                    if next_val < 2**31 and S[k:].startswith(next_s):
                        fibs.append(next_val)
                        k += len(next_s)
                    else:
                        break
                if k == n and len(fibs) >= 3:
                    return fibs
        return []
                

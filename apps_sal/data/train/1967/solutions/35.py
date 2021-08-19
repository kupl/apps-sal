class Solution:

    def splitIntoFibonacci(self, S: str) -> List[int]:
        for i in range(len(S)):
            x = S[:i + 1]
            if x != '0' and x.startswith('0'):
                break
            a = int(x)
            for j in range(i + 1, len(S)):
                y = S[i + 1:j + 1]
                if y != '0' and y.startswith('0'):
                    break
                b = int(y)
                fib = [a, b]
                k = j + 1
                while k < len(S):
                    nxt = fib[-1] + fib[-2]
                    nxtS = str(nxt)
                    if nxt <= 2 ** 31 - 1 and S[k:].startswith(nxtS):
                        k += len(nxtS)
                        fib.append(nxt)
                    else:
                        break
                else:
                    if len(fib) >= 3:
                        return fib
        return []

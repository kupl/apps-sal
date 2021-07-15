class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        for i in range(len(S))[::-1]:
            for j in range(i+1,len(S)):
                b,c = int(S[i:j]), int(S[j:])
                if c >= 2**31: continue
                if b >= 2**31: continue

                parts = [b,c]
                a = c-b
                while a >= 0 and a <= 2**31 - 1:
                    parts.insert(0, a)
                    b,c = a,b
                    a = c-b

                    if S == ''.join(map(str,parts)):
                        return parts
        
        return []

class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        def split(N,s):
            if not s: 
                return N

            c = sum(N[-2:])
            if s.startswith(str(c)):
                return split(N + [c], s[len(str(c)):])

        for i in range(1,len(S)):
            for j in range(i+1, len(S)):
                a = int(S[:i])
                b = int(S[i:j])
                if str(a) == S[:i] and str(b) == S[i:j]:
                    ans = split([a, b], S[j:])
                    if ans and all(x<=2**31-1 for x in ans):
                        return ans
                
        return []

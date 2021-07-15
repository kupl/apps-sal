class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:

        def count(s):
            alpha = [0] * 26
            for w in s:
                alpha[ord(w) - ord('a')] += 1
            return tuple(alpha)
        
        def compare(a, b):
            for i in range(26):
                if b[i] > a[i]:
                    return False
            return True
        
        Acount = [count(a) for a in A]
        Bcount = [0] * 26
        
        for b in B:
            tmp = count(b)
            for i in range(26):
                Bcount[i] = max(Bcount[i], tmp[i])
        Bcount = tuple(Bcount)
        
        res = []
        
        for i in range(len(Acount)):
            if all(Acount[i][j] >= Bcount[j] for j in range(26)):
                res.append(A[i])
        return res

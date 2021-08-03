class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        m = {}
        for i in range(26):
            letter = chr(ord('a') + i)
            m[letter] = 0
            for w in B:
                ct_curr_l = 0
                for l in w:
                    if l == letter:
                        ct_curr_l += 1
                m[letter] = max(m[letter], ct_curr_l)
        res = []
        for w in A:
            A_m = {}
            rt = True
            for l in w:
                if not l in A_m:
                    A_m[l] = 0
                A_m[l] += 1
            for k in m:
                if m[k] > 0 and ((k not in A_m) or (A_m[k] < m[k])):
                    rt = False
            if rt == True:
                res.append(w)
        return res

class Solution:
    def longestAwesome(self, S: str) -> int:
        P = [0]
        for c in S:
            x = int(c)
            P.append(P[-1])
            P[-1] ^= 1 << x
        
        first = {} # first[mask] = i the lowest i with P[i] = mask
        valid = {1 << x for x in range(10)}
        print(valid)
        valid.add(0)
        
        ans = 0
        for j, q in enumerate(P):
            for target in valid:
                i = first.get(q ^ target, None)
                if i is not None:
                    ans = max(ans, j - i)
            first.setdefault(q, j)
        
        return ans

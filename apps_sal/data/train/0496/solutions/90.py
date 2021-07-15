from collections import defaultdict

class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        H = defaultdict(int)
        for a in A:
            H[a] += 1
            
        V = sorted(H.keys())
        
        ans = 0
        while True:
            if len(H) == 0:
                return ans
            elif len(H) == 1:
                v = min(H.keys())
                ans += (H[v] - 1) * H[v] // 2
                del H[v]
                del V[0]
            else:
                v1, v2 = V[0], V[1]
                if v1 + H[v1] - 1 < v2:
                    ans += (H[v1] - 1) * H[v1] // 2
                    del H[v1]
                    del V[0]
                else:
                    ans += (v2 - v1 - 1) * (v2 - v1) // 2
                    ans += (H[v1] - v2 + v1) * (v2 - v1)
                    H[v2] += (H[v1] - v2 + v1)
                    del H[v1]
                    del V[0]
                    



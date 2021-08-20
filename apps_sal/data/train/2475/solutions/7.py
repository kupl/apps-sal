class Solution:

    def minDeletionSize(self, A: List[str]) -> int:
        D = 0
        for col in zip(*A):
            p = chr(0)
            for c in col:
                if c < p:
                    D += 1
                    break
                p = c
        return D

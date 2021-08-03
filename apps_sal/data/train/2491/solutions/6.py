class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        count_A = {}
        doubled = False
        for i, a in enumerate(A):
            if a not in count_A:
                count_A[a] = set()
            else:
                doubled = True
            count_A[a].add(i)
        off = 0
        for i, b in enumerate(B):
            if b not in count_A:
                return False
            else:
                if i in count_A[b]:
                    count_A[b].remove(i)
                    if not count_A[b]:
                        del count_A[b]
                else:
                    off += 1
                    if off > 2:
                        return False
        return doubled or off == 2

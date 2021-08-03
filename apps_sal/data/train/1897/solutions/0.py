from itertools import accumulate


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xors = [0]
        for a in arr:
            xors.append(a ^ xors[-1])
        return [xors[i] ^ xors[j + 1] for i, j in queries]

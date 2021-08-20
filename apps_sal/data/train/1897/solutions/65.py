from itertools import accumulate
import operator


class Solution:

    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        x = list(accumulate(arr, operator.__xor__, initial=0))
        return [x[i] ^ x[j + 1] for (i, j) in queries]

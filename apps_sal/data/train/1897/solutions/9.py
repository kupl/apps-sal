class Solution:
    #     def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
    #         ans = []
    #         pool = dict()
    #         for r in queries:
    #             if tuple(r) in pool:
    #                 ans.append(pool[tuple(r)])
    #             else:
    #                 pool[tuple(r)] = reduce(lambda x,y: x^y, arr[r[0]:r[1]+1])
    #                 ans.append(pool[tuple(r)])
    #         return ans

    # fact: xor[i,j] = xor[0,i] ^ xor[0,j]
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        # prefix the arr
        for i in range(1, len(arr)):
            arr[i] ^= arr[i - 1]
        return [arr[j] ^ arr[i - 1] if i > 0 else arr[j] for i, j in queries]

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        store = {}
        n = len(arr)
        curr = 0
        store[-1] = 0
        for i in range(n):
            curr ^= arr[i]

            store[i] = curr

        return [store[b] ^ store[a - 1] for a, b in queries]

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        arr.insert(0, 0)
        for i in range(1, len(arr)):
            arr[i] ^= arr[i - 1]
        return [arr[a] ^ arr[b + 1] for a, b in queries]

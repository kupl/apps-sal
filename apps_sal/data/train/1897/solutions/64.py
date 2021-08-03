class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(1, len(arr)):
            arr[i] = arr[i - 1] ^ arr[i]
        return [arr[j] if i == 0 else arr[i - 1] ^ arr[j] for i, j in queries]

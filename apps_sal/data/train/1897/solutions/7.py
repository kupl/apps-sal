class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(1, len(arr)):
            arr[i] ^= arr[i - 1]
        result = []
        for x, y in queries:
            if x == 0:
                result.append(arr[y])
            else:
                result.append(arr[y] ^ arr[x - 1])
        return result


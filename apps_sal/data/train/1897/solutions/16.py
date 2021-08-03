class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        if len(arr) == 0:
            return []

        xor_arr = [0 for i in range(len(arr))]
        for index, v in enumerate(arr):
            if index == 0:
                xor_arr[index] = arr[index]
            else:
                xor_arr[index] = xor_arr[index - 1] ^ arr[index]
        results = [0 for i in range(len(queries))]
        for index, query in enumerate(queries):
            start = query[0]
            end = query[1]
            if start == 0:
                results[index] = xor_arr[end]
            else:
                results[index] = xor_arr[end] ^ xor_arr[start - 1]
        return results

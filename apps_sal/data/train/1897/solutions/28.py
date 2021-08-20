class Solution:

    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        acc = [0]
        for i in range(len(arr)):
            acc.append(acc[i] ^ arr[i])
        result = []
        for q in queries:
            result.append(acc[q[0]] ^ acc[q[1] + 1])
        return result

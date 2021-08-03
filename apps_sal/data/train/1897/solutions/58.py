class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefixSum = [0] * len(arr)
        prefixSum[0] = arr[0]
        result = []
        for i in range(1, len(arr)):
            prefixSum[i] = prefixSum[i - 1] ^ arr[i]
        for i in queries:
            if(i[0] == 0):
                result.append(prefixSum[i[1]])
                continue
            result.append(prefixSum[i[1]] ^ prefixSum[i[0] - 1])
        return(result)

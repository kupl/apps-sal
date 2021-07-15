class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        result =[]
        prefixArr = [0] * len(arr)
        prefixArr[0] = arr[0]
        for i in range(1, len(arr)):
            prefixArr[i] = prefixArr[i-1] ^ arr[i]
        
        for j in range(len(queries)):
            start = queries[j][0]
            end = queries[j][1]
            
            if start == 0: result.append(prefixArr[end])
            else: result.append(prefixArr[start - 1] ^ prefixArr[end] )
        
        return result     


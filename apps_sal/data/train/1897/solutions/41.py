class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        #the poor way to do this is to just go through and Xor the
        res = []
        for i in range(1,len(arr)):
            arr[i] ^= arr[i-1]
        for i,j in queries:
            if i == 0:
                res.append(arr[j])
            else:
                res.append(arr[i-1] ^ arr[j])
        return res #so this is the absurdly slow way to do it though we should be able to memoize in some way?


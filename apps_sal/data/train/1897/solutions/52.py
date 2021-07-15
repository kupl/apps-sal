class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        if arr == []:
            return []
        res=[]
        pre=[arr[0]]
        for i in range(1,len(arr)):
            pre.append(arr[i]^pre[-1])
            
        for i in range(0,len(queries)):
            xor=0
            if queries[i][0] == queries[i][1]:
                res.append(arr[queries[i][0]])
            elif (abs(queries[i][0] - queries[i][1]) == 1):
                res.append(arr[queries[i][0]] ^ arr[queries[i][1]])
            else:
                if queries[i][0] == 0:
                    res.append(pre[queries[i][1]])
                else:
                    res.append(pre[queries[i][1]]^pre[queries[i][0]-1])
        print(res)
        return(res)
                    
                


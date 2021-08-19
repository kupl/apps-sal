class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # result=[]
        # for i in range(len(queries)):
        #     start=queries[i][0]
        #     end=queries[i][1];val=arr[start]
        #     while start != end+1:
        #         if start!=end:
        #             val=val^arr[start+1]
        #             start+=1
        #         else:
        #             result.append(val)
        #             break
        # return result

        prefix = [None] * len(arr)
        res = [None] * len(queries)
        prefix[0] = arr[0]
        for i in range(1, len(arr)):
            prefix[i] = prefix[i - 1] ^ arr[i]
        for i in range(len(queries)):
            if queries[i][0] == 0:
                res[i] = prefix[queries[i][1]]
                continue
            res[i] = prefix[queries[i][1]] ^ prefix[queries[i][0] - 1]
        return res

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        lookup=[0]*len(arr)
        lookup[0]=arr[0]
        for i in range(1,len(arr)):
            lookup[i] = lookup[i-1]^arr[i]

        r=[]
        for i in range(len(queries)):
            if queries[i][0]==0:
                r.append(lookup[queries[i][1]])
            else:
                tmp=lookup[queries[i][1]]^lookup[queries[i][0]-1]
                r.append(tmp)
        return r

        \"\"\"\"\"\"
        r=[]
        for i in range(len(queries)):
            
            tmp=arr[queries[i][0]:queries[i][1]+1]
            #print(tmp)
            s= tmp[0]
            if len(tmp) >1:
                for i in range(1,len(tmp)):
                    s=s^tmp[i]
            #print(s)
            #print(\"----\")
            r.append(s)
        return r
        \"\"\"\"\"\"

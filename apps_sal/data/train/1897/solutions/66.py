class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        a = [arr[0],]
        for i in range(1,len(arr)):
            a.append(arr[i]^a[i-1])
        for q in queries:
            if(q[0]==0):
                ans.append(a[q[1]])
            else:
                ans.append(a[q[1]]^a[q[0]-1])
        return ans


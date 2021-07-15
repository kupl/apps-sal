class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        q=deque([])
        ans=[]
        for i in range(1,m+1,1):
            q.append(i)
            
        for j in queries:
            ans.append(q.index(j))
            q.remove(j)
            q.appendleft(j)
        
        return ans

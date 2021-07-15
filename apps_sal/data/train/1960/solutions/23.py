class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        ans = []
        arr = list(range(1,m+1))
        
        for j in queries:
            for i in range(m):
                if j==arr[i]:
                    ans.append(i)
                    x = arr.pop(i)
                    arr.insert(0, x)
        
        return ans
                
            


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P=deque([i for i in range(1,m+1)])
        ans=[]
        for q in queries:
            new_P = deque()
            for index, p in enumerate(P):
                if p != q:
                    new_P.append(p)
                else:
                    ans.append(index)
            new_P.appendleft(q)
            P = new_P
        return ans

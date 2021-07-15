class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        q=[]
        p= max(arr) + k
        for i in range(1,p+1):
            if i not in arr:
                q.append(i)
        print(q)
        
        return(q[k-1])
                


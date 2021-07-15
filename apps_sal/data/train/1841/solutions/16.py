class Solution:
    def getStrongest(self, lis: List[int], k: int) -> List[int]:
        n = len(lis)
        lis.sort()
        med = lis[(n-1)//2]
        ans=[[abs(med-lis[i]),lis[i]] for i in range(n)]
        ans.sort(reverse = True)
        fin=[]
        for i in range(k):
            fin.append(ans[i][1])
        return fin


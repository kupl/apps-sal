class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        lo=[i for i in range(2,n+1)]
        hi=[i for i in range(1,n)]
        res=[]
        dic=[]
        for i in range(len(lo)):
            for j in range(len(hi)):
                if hi[j]/lo[i] not in dic and hi[j]<lo[i]:
                    dic.append(hi[j]/lo[i])
                    res.append(str(hi[j])+\"/\"+str(lo[i]))
        return res

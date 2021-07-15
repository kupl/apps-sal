class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # d=dict()
        # res=0
        # for i,j in dominoes:
        #     if(str([i,j]) in d):
        #         d[str([i,j])]+=1
        #         res+=d[str([i,j])]
        #     elif(str([j,i]) in d):
        #         d[str([j,i])]+=1
        #         res+=d[str([j,i])]
        #     else:
        #         d[str([i,j])]=0
        # return res
        d={}
        res=0
        for i in dominoes:
            i=sorted(i)
            if(str(i) not in d):
                d[str(i)]=0
            d[str(i)]+=1
            if(d[str(i)]>1):
                res+=d[str(i)]-1
        print(d)
        return res

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lucky=-1
        op={}
        for i in arr:
            if i not in op:
                op[i]=1
            else:
                op[i]+=1
            
        for k,v in list(op.items()):
            if k == v:
                if k >= lucky:
                    lucky=k
        return lucky


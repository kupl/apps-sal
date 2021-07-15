class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        r=[]
        t=0
        i=1
        while len(r)<k:
            if i not in arr:
                t+=1
                r.append(i)
            i+=1
        return r[-1]

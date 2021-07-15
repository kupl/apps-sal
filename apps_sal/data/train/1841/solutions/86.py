class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        x= sorted(arr)
        m=x[int((len(x)-1)/2)]
        i=0
        j=len(arr)-1
        strong=[]
        while (i<=j):
            if abs(x[i]-m) <= abs(x[j]-m):
                strong.append(x[j])
                j-=1
            else:
                strong.append(x[i])
                i+=1
                
        return strong[:k]


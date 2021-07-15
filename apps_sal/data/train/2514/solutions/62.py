class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr1.sort()
        arr2.sort()
        m=len(arr1)
        n=len(arr2)
        cnt=0
        for i in range(m):
            flag=True
            for j in range(n):
                dis=abs(arr1[i]-arr2[j])
                if(dis<=d):
                    flag=False
                    break
            if(flag):
                cnt+=1
                
        return cnt



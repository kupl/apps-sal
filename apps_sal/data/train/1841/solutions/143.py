class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        if len(arr)==1 and k==1:
            return(arr)
        ans=[]
        arr.sort()
        m=arr[(len(arr)-1)//2]
        i, j=0, len(arr)-1
        while i<=j:
            if abs(arr[j]-m)>=abs(arr[i]-m):
                ans.append(arr[j])
                j-=1
            else:
                ans.append(arr[i])
                i+=1
        print(ans)
        return(ans[:k])

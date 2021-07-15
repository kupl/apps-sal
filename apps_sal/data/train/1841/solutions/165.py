class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        median = arr[(len(arr)-1)//2]
        ans,i,j = [],0,len(arr)-1
        if(len(arr) == 1):
            return arr
        
        while(i<=j and k>0):
            if(abs(arr[i]-median) > abs(arr[j]-median)):
                ans.append(arr[i])
                i +=1
            else:
                ans.append(arr[j])
                j-=1
            
            k -=1
        
        return ans

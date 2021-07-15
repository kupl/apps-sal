class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        
        inds = [n%2 for n in arr]
        
        temp =[]
        for i, v in enumerate(inds):
            if v==1:
                temp.append(i)
                     
        if len(temp)<3:
            return False
        
        for i in range(1, len(temp)-1):
            if (temp[i]-temp[i-1]==1) and (temp[i+1]-temp[i]==1):
                return True
        return False
            


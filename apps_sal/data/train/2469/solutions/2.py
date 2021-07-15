class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr2=list([x*2 for x in arr])
        zeros=arr.count(0)
        
        if zeros >=2: return True
        
        
        print(arr2)
        for a in arr2:
            if a in arr: 
                if a==0 and zeros == 1: continue
                return True
        
        return False
    
        


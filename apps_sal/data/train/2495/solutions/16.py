class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if len(target)!=len(arr):
            return False
        
        p=0
        a=sorted(arr)
        t=sorted(target)
        while(p<len(t)):
            if a[p]!=t[p]:
                return False
            p+=1
        
        return True

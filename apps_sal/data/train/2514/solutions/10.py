class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        qual = []
        
        for k in set(arr1):
            if False not in [True if abs(k-k2)>d else False for k2 in set(arr2)]:
                qual.append(k)
        
        k=0
        
        for q in qual:
            k+=arr1.count(q)
        
        return k
        
        
        


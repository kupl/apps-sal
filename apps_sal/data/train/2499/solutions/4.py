class Solution:
    
    def fill(self,A,B):
        for i in range(len(A)):
            B[A[i]] +=1
        return list(filter(lambda a : a != 0,B))
    
    def mcd(self,arr):
        MCD = min(arr)
        for i in range (1,len(arr)):
            MCD = math.gcd(MCD,arr[i])
        return MCD
            
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) < 2:
            return False
        deck.sort()
        B = [0] * (max(deck) + len(deck))
        B = self.fill(deck,B)
        
        for i in range(len(B)-1):
            if B[i] == 1 :
                return False
            
        MCD = self.mcd(B)
        if MCD == 1:
            return False
        
        return True

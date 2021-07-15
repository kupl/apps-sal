class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        m = [ 0 for i in range(1000)]
        
        for x in trips:
            if  x[0] > capacity:
                return False
            
            for i in range(x[1],x[2]):
                m[i]+=x[0]
            
            if max(m)> capacity:
                return False
        
        if max(m) > capacity:
            return False
        return True
                


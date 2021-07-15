class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.prearr = [[] for _ in range(max(arr)+1)]
        
        for i in range (len(arr)):
            try:
                self.prearr[arr[i]].append(i) 
            except:
                print((arr[i],len(self.prearr),max(arr)))
            
    def query(self, left: int, right: int, threshold: int) -> int:   
        prearr = self.prearr
        
        def checkmajority (k):
            
            #find index of left element 
            lo = 0 
            hi= len(prearr[k])-1
            
            while (lo<hi):
                mid = lo +((hi-lo)//2)
                
                if (prearr[k][mid]>=left):
                    hi = mid 
                    
                else:
                    lo = mid+1
                    
            start = lo
            
            #find index of right element 
            lo = 0 
            hi = len(prearr[k])-1
            
            while(lo<hi):
                mid = lo + ((hi-lo +1)//2)
                
                if(prearr[k][mid] <= right):
                    lo = mid
                else:
                    hi = mid-1 
            end = lo 
            
            # return the difference between indexes between the preaar element and compare it with threshold 
            
            if ((end - start +1) >= threshold): 
                return (True)
            
            else:
                return (False)
            
            
        #pick random element from arr 30-50 times and check if it is majority or not
        
        res = False
        a = self.arr[left:right+1]
        
        for _ in range (20): 
            k = random.choice(a)
            res = res or checkmajority(k)
            
            if (res):
                return(k)
        
        return(-1)      
        
        

# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)


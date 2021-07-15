class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        # need to get the distance of each points
        # need to keep the K smallest, then pq can pop the samllest
        # need to negative the input and pushpop so that i can do the k operation
        
        # other approach would be quick_select
        # by randomize the input, you can get the average O(n) worst case O(n**2)
        # get the parition of input arr, 
        # if partition < k: quick_select(st, partition-1)
        # else: quick_select(partition+1, end)
        
        def parition(st, end):
            
            lo, i, j = st, st, end
            while True:
                
                while i < end and arr[i][0] <= arr[lo][0]:
                    i+=1
                
                while j > st and arr[lo][0] <= arr[j][0]:
                    j-=1
                    
                if i >= j:
                    break
                arr[i], arr[j] = arr[j], arr[i]
            arr[lo], arr[j] = arr[j], arr[lo]
            return j
        
        def quick_select(st, end):
            
            # this gurantee 0,1. 1,1 is not possible
            if st > end:
                return
            
            par = parition(st, end)
            
            if par == K:
                return
            
            if par > K:
                quick_select(st, par-1)
            else:
                quick_select(par+1, end)
            return 
        
        arr = []
        for pt in points:
            arr.append( [math.sqrt(sum([x**2 for x in pt])), pt] )
        #print(arr)
        random.shuffle(arr)
        #print(arr)
        quick_select(0, len(arr)-1)
        
        return [x[1] for x in arr[:K]]

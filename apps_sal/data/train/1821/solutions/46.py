class Solution:
    
    def merge(self,low,mid,high,arr):
        
        left = []
        right = []
        
        l_limit = mid+1-low
        r_limit = high+1-mid-1
        
        for i in range(low, mid+1):
            left.append(arr[i])
        
        for i in range(mid+1, high+1):
            right.append(arr[i])
            
        #print(\"During merge arrays are \", left, right)
        #print(\"limits are \",l_limit, r_limit)
        
        #using left and right as temp variables, merge it onto arr
        
        l_iter = 0
        r_iter = 0
        
        filler = low
        
        while(l_iter < l_limit or r_iter < r_limit):
            
            if(l_iter == l_limit):
                arr[filler] = right[r_iter]
                r_iter+=1
            elif(r_iter == r_limit):
                arr[filler] = left[l_iter]
                l_iter+=1
            elif(left[l_iter] < right[r_iter]):
                arr[filler] = left[l_iter]
                l_iter+=1
            else:
                arr[filler] = right[r_iter]
                r_iter+=1
                
            filler+=1
            #print(l_iter, r_iter, l_limit, r_limit)
            
    def mergeSort(self,arr, low, high):
        
        if(low < high):
            
            mid = low + (high-low)//2
            
            #print(\"mergesort for \", arr[low:mid+1], arr[mid+1:high+1])
            
            self.mergeSort(arr, low, mid) #from low to mid
            self.mergeSort(arr, mid+1, high) #from mid+1 to high
            
            self.merge(low,mid,high,arr)
    
    def sortArray(self, arr: List[int]) -> List[int]:
            
        n = len(arr)
        
        if(n==1):
            return arr
        else:
            self.mergeSort(arr, 0,n-1)
            return arr


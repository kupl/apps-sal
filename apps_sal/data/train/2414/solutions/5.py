class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        #print(arr)
        #print(a)
        #print(b)
        #print(c)
        count = 0
        lis = []
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j+1,len(arr)):
                        if abs(arr[j] - arr[k])<= b and abs(arr[i] - arr[k]) <= c:
                            lis.append((arr[i],arr[j],arr[k]))
        return(len(lis))
        
                        
                    
                   
                    #if abs(arr[i] - arr[j]) <= a  and  abs(arr[j] - arr[k]) <= b and  abs(arr[i] - arr[k]) <= c:
                        
                     
                        #lis.append((arr[i],arr[j],arr[k]))
        #print(lis)
                        
                        
            
                        


def LCM(arr, n): 
      
   
    max_num = 0; 
    for i in range(n): 
        if (max_num < arr[i]): 
            max_num = arr[i]

    res = 1; 
  
    x=2
    while (x <= max_num): 
          

        indexes = []; 
        for j in range(n): 
            if (arr[j] % x == 0): 
                indexes.append(j)
  
        if (len(indexes) >= 2): 
              
            
            for j in range(len(indexes)): 
                arr[indexes[j]] = int(arr[indexes[j]] / x)
  
            res = res * x
        else: 
            x += 1; 
  
  
    for i in range(n): 
        res = res * arr[i]
        
  
    return res+r
t=int(input())
for i in range(0,t):

    n=int(input())
    arr=list(map(int,input().split()))
    r=int(input())
    print(LCM(arr, n))
    
    



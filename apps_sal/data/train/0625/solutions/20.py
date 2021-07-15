# cook your dish here
def subCount(arr, n, k=10): 
 
    mod =[] 
    for i in range(k + 1): 
        mod.append(0) 
    cumSum = 0
    for i in range(n): 
        cumSum = cumSum + arr[i] 

        mod[((cumSum % k)+k)% k]= mod[((cumSum % k)+k)% k] + 1
      
    
    result = 0  # Initialize result 
       
    # Traverse mod[] 
    for i in range(k): 
        if (mod[i] > 1): 
            result = result + (mod[i]*(mod[i]-1))//2

    result = result + mod[0] 
       
    return result 
    
for t_itr in range(0,int(input())):
    n = int(input())
    a = list(map(str, input().split()))
    b = []
    for i in a:
        b.append(int(i[0]))
    result = subCount(b, n, 10)
    print(result)
    


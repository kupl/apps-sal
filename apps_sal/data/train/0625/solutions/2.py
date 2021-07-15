def subCount(arr, n, k): 
    mod =[] 
    for i in range(k + 1): 
        mod.append(0) 
    cumSum = 0
    for i in range(n): 
        cumSum = cumSum + arr[i] 
        mod[((cumSum % k)+k)% k]= mod[((cumSum % k)+k)% k] + 1
    result = 0 
    for i in range(k): 
        if (mod[i] > 1): 
            result = result + (mod[i]*(mod[i]-1))//2
    result = result + mod[0] 
    return result 
def inp(x):
    return int(x.rstrip('0'))
def main(t):
    k = 10
    n = int(input())  
    arr =  list(map(inp,input().split()))
    print(subCount(arr, n, k))   
    if t>1:
        main(t-1)
main(int(input())) 


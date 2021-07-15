def maxCircularSum(arr, n, k) : 
    sum = 0
    start = 0
    end = k - 1  
    for i in range(k) : 
        sum += arr[i] 
    ans = sum  
    for i in range(k, n + k) :  
        sum += arr[i % n] - arr[(i - k) % n] 
        if (sum > ans) : 
            ans = sum  
            start = (i - k + 1) % n  
            end = i % n 
    print(ans)   
t = int(input())
for i in range(t):
    lst1 = input().split()
    n = int(lst1[0])
    k = int(lst1[1])
    lst = input().split()
    lst = [int(l) for l in lst]
    maxCircularSum(lst, n, k) 

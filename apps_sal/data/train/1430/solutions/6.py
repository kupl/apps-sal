t = int(input())
while t != 0:
    n, k = list(map(int, input().split()))
    
    if n% 2 == 0 :
        even = n/2 
        odd = n/2 * (k+1)
#         print("even",even,"odd",odd)
    else:
        odd = (n-1)/2 * (k+1)
        even = (n-1)/2 + (1 + 2*k)
#         print("even",even,"odd",odd)
    total = even + odd
    print(int(total))
          
    t -= 1

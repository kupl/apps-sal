n = int(input())

l1 = 1
l2 = 1

ans = 0

if(n == 0):
    ans = 0
elif(n == 1):
    ans = 1
elif(n == 2):
    ans = 2
else:
    ans = 2
    for i in range(3,n+1):
        ans = ans % 15746
        k = l2 
        l2 = ans
        l1 = k
        ans = l1 + l2

ans = ans % 15746
        
print(ans)

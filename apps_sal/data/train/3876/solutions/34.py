def find(n):
    ans = 0
    for i in range(0,n+1):
        if i % 3 == 0:
            ans = ans + i
        elif i % 5== 0:
            ans = ans + i
    return ans        

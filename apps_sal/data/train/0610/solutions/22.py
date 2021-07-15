t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    
    one = [i for i, x in enumerate(arr) if x == 1]
    
    flag = 0
    
    for i in range(1, len(one)):
        if(one[i]-one[i-1] < 6):
            flag = 1
            break
    
    if(flag == 1):
        print("NO")
    else:
        print("YES")

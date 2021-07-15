import math
test = int(input())
for _ in range(test):
    n = int(input())
    array = list(map(int, input().split()))
    hcf = array[0]
    for i in range(1, n):
        hcf = math.gcd(hcf, array[i])
    
    if hcf==1:
        print(-1)
    elif hcf%2==0:
        print(2)
    else:
        answer=0
        for i in range(3, int((hcf)**0.5) +1):
            if hcf%i==0:
                answer = i
                break
        if answer==0:
            print(hcf)
        else:
            print(answer)

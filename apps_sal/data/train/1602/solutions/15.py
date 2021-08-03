T = int(input())
while T:
    n = int(input())
    x = int(input())
    A = list(map(int, input().split()))
    A.sort()
    flag = True
    i = 0
    temp = 1
    while i < n:
        for j in range(i, min(i + x, n)):
            if(A[j] <= temp):
                flag = False
                break
        temp += 1
        i += x
    if(flag):
        print("Possible")
    else:
        print("Impossible")
    T -= 1

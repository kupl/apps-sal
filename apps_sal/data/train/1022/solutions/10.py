T = int(input())
for i in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    x = N // 2
    c = 0
    if(N % 2 != 0):
        print("NO")
    else:
        for i in range(x):
            if(A[i] == -1 and A[i + x] == -1):
                A[i] = 1
                A[i + x] = 1
            elif(A[i] == -1):
                A[i] = A[i + x]
            elif(A[i + x] == -1):
                A[i + x] = A[i]
        for i in range(x):
            if(A[i] != A[i + x]):
                c = 1
                break
        if(c == 1):
            print("NO")
        else:
            print("YES")
            print(*A)

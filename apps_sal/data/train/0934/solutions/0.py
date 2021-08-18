T = int(input())
for i in range(T):
    n = list(map(int, input().split()))
    a = n[0]
    b = n[1]
    c = n[2]
    l = []
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    for i in range(b):
        for j in range(a):
            for k in range(c):
                if(A[j] <= B[i] and B[i] >= C[k]):
                    sum = ((A[j] + B[i]) * (B[i] + C[k]))
                    l.append(int(sum))

    sum = 0
    for i in range(len(l)):
        sum += int(l[i])
    print(sum % 1000000007)

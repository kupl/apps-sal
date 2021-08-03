import math
T = int(input())
while T:
    N = int(input())
    A = list(map(int, input().split()))
    hcf = A[0]
    n = len(A)
    for i in range(1, len(A)):
        hcf = math.gcd(hcf, A[i])
    if hcf == 1:
        print(-1)
    elif hcf % 2 == 0:
        print(2)
    else:
        answer = 0
        for j in range(3, int(hcf ** 0.5) + 1):
            if hcf % j == 0:
                answer = j
                break
        if answer == 0:
            print(hcf)
        else:
            print(answer)
    T -= 1

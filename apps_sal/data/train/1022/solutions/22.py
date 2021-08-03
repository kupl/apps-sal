T = int(input())
n = 0
for i in range(T):
    c = 0
    n = int(input())
    A = list(map(int, input().strip().split(" ")))
    if(n % 2 == 1):
        print('NO')
        continue
    for j in range(int(n / 2)):
        if A[j] == -1 and A[int(j + n / 2)] != -1:
            A[j] = A[int(j + n / 2)]
        elif A[j] != -1 and A[int(j + n / 2)] == -1:
            A[int(j + n / 2)] = A[j]
        elif A[j] == -1 and A[int(j + n / 2)] == -1:
            A[j] = 1
            A[int(j + n / 2)] = 1
            continue

    for j in range(int(n / 2)):
        if A[j] != A[int(j + n / 2)]:
            c = 1
            break
    if c == 1:
        print('NO')
    else:
        print('YES')
        print(" ".join(map(str, A)))

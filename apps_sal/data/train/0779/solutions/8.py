def Average(A, B):
    return (A + B) / 2


T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    while(len(A) != 1):
        A.insert(0, Average(A.pop(0), A.pop(0)))
    print(A[0])

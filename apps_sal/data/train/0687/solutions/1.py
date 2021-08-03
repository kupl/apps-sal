def no_total(A):
    for i in range(len(A)):
        for j in range(i + 2, len(A)):
            if (A[i] > A[j]):
                return False
    return True


cases = int(input())
for case in range(cases):
    n = int(input())
    A = list(map(int, input().split()))
    if (no_total(A)):
        print("YES")
    else:
        print("NO")

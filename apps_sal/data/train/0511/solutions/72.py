n = int(input())
A = list(map(int, input().split()))
x = A[0]
for a in A[1:]:
    x = x ^ a
for a in A:
    print(a^x, end=" ")

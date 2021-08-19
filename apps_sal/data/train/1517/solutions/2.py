t = int(input())
for i in range(t):
    (value, k) = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    newValue = value
    for j in range(k):
        temp = newValue * float(A[j]) / B[j]
        newValue += temp
    error = value * 100 / newValue
    print(int(100 - error))

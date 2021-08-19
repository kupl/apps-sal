from fractions import gcd as G
n = eval(input())
flag = 1
arr = list(map(int, input().split()))
a = max(arr)
best = 0
I_I = 0
while I_I < n:
    if arr[I_I] == a:
        k = I_I
        while k < n and arr[k] == a:
            k += 1
        best = max(best, k - I_I)
        I_I = k
    else:
        I_I += 1
print(best)

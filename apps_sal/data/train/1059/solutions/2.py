N = int(input())
A = {}
largest = 0

for m in range(0, N):
    p = int(input())
    A[p] = 0

for k in A:
    for m in A:
        if k % m > largest:
            largest = k % m

print(largest)

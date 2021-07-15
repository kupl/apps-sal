n = int(input())
A = list(map(int, input().split()))

m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1

    left = y
    right = A[x] - left - 1
    
    A[x] = 0
    
    if x - 1 >= 0:
        A[x - 1] += left
    if x + 1 < n:
        A[x + 1] += right
    
for a in A:
    print(a)

from sys import stdin

t = int(stdin.readline().strip())
for i in range(t):
    n = int(stdin.readline().strip())
    A = list(map(int, stdin.readline().strip().split(' ')))
    i = n - 2
    while i >= 0 and A[i] >= A[i + 1]:
        i -= 1
    while i >= 0 and A[i] <= A[i + 1]:
        i -= 1
    print(i + 1)

n, k = list(map(int, input().split()))
A = list(map(int, input().split()))
maximum = max(A)
minimum = min(A)
if k == 0:
    for i in A:
        print(i, end=' ')
elif k & 1:
    for i in A:
        print(maximum - i, end=' ')
else:
    for i in A:
        print(i - minimum, end=' ')

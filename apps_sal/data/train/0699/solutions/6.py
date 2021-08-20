T = int(input())
for i in range(T):
    (n, k, d) = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    s = sum(A)
    if s // k < d:
        print(s // k)
    else:
        print(d)

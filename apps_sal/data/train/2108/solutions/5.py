(n, m) = input().split()
k = int(input())
print(n, m)
for i in range(k):
    (nn, nm) = input().split()
    if nn == n:
        n = nm
    else:
        m = nm
    print(n, m)

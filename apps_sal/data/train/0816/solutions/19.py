

n = int(input())
a = list(map(int, input().split()))
q = int(input())
for i in range(q):
    k = int(input())
    print(a[k - 1])
    a.pop(k - 1)

T = int(input())
for i in range(T):
    N = int(input())
    a = sorted(list(map(int, input().split())), reverse=True)
    c = a[len(a) - 1]
    a.remove(a[0])
    b = len(a) * c
    print(b)

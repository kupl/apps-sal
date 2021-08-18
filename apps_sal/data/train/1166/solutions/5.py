n = int(input())
a = list(map(int, input().split()))
q = int(input())
for i in range(q):
    k = int(input())
    x = 0
    for i in range(0, len(a)):
        for j in range(i, len(a)):
            if k == min(a[i:j + 1]):
                x = x + 1
    print(x)

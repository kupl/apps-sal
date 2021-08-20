n = int(input())
l = list(map(int, input().split()))
print(1, end=' ')
ptr = n - 1
v = [0] * n
for i in range(n):
    v[l[i] - 1] = 1
    while ptr >= 0 and v[ptr] == 1:
        ptr -= 1
    print(i + 1 - (n - 1 - ptr) + 1, end=' ')

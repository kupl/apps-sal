input()
a = input().split()
cnt = 0
while len(a) > 0:
    k = a[1:].index(a[0]) + 1
    cnt += k - 1
    a = a[1:k] + a[k + 1:]
print(cnt)

# cook your dish here
n = int(input())
a, h = [], []
arr = [list(map(int, input().split())) for i in range(n)]
arr = sorted(arr, key=lambda i: i[0])
for i in arr:
    k, m = i
    a.append(k)
    h.append(m)
if n == 1 or n == 2:
    print(n)
else:
    count, chopped = 2, 0
    for i in range(1, n - 1):
        if a[i] - a[i - 1] > h[i] and chopped == 0:
            count += 1
        elif chopped == 1 and a[i] - a[i - 1] - h[i - 1] > h[i]:
            chopped = 0
            count += 1
        elif a[i + 1] - a[i] > h[i]:
            count += 1
            chopped = 1
        else:
            chopped = 0
    print(count)

m = int(input())
q = list(map(int, input().split()))
n = int(input())
a = list(map(int, input().split()))
q.sort()
a.sort()
j = n - 1
i = 0
ans = 0
while j >= 0:

    for i in range(q[0]):
        ans = ans + a[j]
        j = j - 1
        if j < 0:
            break
    j = j - 2
print(ans)

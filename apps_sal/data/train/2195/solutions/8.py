n = int(input())

a = list(map(int,input().split(' ')))

z = {}

for i in range(n):
    if a[i] not in z:
        z[a[i]] = 1
    else:
        z[a[i]] +=1

ans = n


s = sorted(z.values())

ans = ans - max(s)

print(ans)


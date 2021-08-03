n = int(input())

p = [int(x) for x in input().split()]

mx = n

a = [0] * (n + 1)

ans = [1]

for i in range(0, n):

    t = p[i]

    a[t] = 1

    while a[mx] == 1 and mx >= 1:
        mx -= 1

    ans.append(i + 1 - (n - mx) + 1)

print(' '.join(map(str, ans)))


# Made By Mostafa_Khaled

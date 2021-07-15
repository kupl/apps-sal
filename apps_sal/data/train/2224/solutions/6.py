n = int(input())
a = [*map(int, list(input()))]
b = [*map(int, list(input()))]
one = sum(a)
zero = len(a) - one
ans = 0
wk1 = 0
wk2 = 0
for i in range(n):
    if b[i] == 0:
        if a[i] == 0:
            ans += one
            wk1 += 1
        else:
            ans += zero
            wk2 += 1
print(ans - wk1 * wk2)

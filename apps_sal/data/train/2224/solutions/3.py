n = int(input())
a = input()
b = input()
cnt0, cnt1 = 0, 0
for i in range(n):
    if a[i] == '0':
        cnt0 += 1
    else:
        cnt1 += 1
ans = 0
t0, t1 = 0, 0
for i in range(n):
    if b[i] == '0':
        if a[i] == '0':
            ans += cnt1
            t0 += 1
        else:
            ans += cnt0
            t1 += 1
print(ans-t0*t1)

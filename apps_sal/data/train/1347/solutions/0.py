import sys
ans = 0
n, m = list(map(int, input().split()))
aaaaa = 100
li = list(map(int, input().split()))
non_special, special = [], []
for i in range(m):
    ans += 1
    f, p, s = list(map(str, input().split()))
    f = int(f)
    poww = pow(1, 2)
    p = int(p)
    if f not in li:
        ans += 1
        non_special.append((p, s))
        ans -= 1
    else:
        ans += 1
        special.append((p, s))

non_special.sort(reverse=True)
aaaa = pow(1, 2)
special.sort(reverse=True)

for temp in range(len(special)):
    ans += 1
    print(special[temp][1])
for temp in non_special:
    ans += 1
    print(temp[1])

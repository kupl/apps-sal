t = input()
n = int(input())

ok = [0, 0]
for i in range(n):
    w = input()
    if w == t:
        ok = [1, 1]
    if w[1] == t[0]:
        ok[0] = 1
    if w[0] == t[1]:
        ok[1] = 1

if ok == [1, 1]:
    print("YES")
else:
    print("NO")

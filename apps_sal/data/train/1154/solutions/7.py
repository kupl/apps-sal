a = input()
b = sorted(input().split())
c = sorted(input().split())
f = 0
for i in range(0, len(b)):
    if c[i] != b[i]:
        print(c[i])
        f = 1
        break
if f == 0:
    print(c[-1])

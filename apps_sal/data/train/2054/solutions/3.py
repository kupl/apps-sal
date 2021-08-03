n = int(input())
a = []
b = []
for i in range(n - 1):
    x, y = list(map(int, input().split()))
    a.append(x)
    b.append(y)

colors = list(map(int, input().split()))


lehet = []
for i in range(n - 1):
    if colors[a[i] - 1] != colors[b[i] - 1]:
        if len(lehet) == 0:
            lehet += [a[i], b[i]]
        else:
            if a[i] in lehet and b[i] in lehet:
                print("NO")
                return
            elif a[i] in lehet:
                lehet = [a[i]]
            elif b[i] in lehet:
                lehet = [b[i]]
            else:
                print("NO")
                return
print("YES")
if len(lehet) == 0:
    lehet = [1]
print(lehet[0])

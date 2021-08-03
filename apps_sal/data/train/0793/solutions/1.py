# cook your dish here
n, r = map(int, input().split())
h = list(map(int, input().split()))
d = [abs(r - h[0])]


def hcf(x, y):
    while(y):
        x, y = y, x % y
    return x


for i in range(len(h) - 1):
    d.append(abs(h[i + 1] - h[i]))
for i in range(len(d) - 1):
    d[i + 1] = hcf(d[i], d[i + 1])
print(d[-1])

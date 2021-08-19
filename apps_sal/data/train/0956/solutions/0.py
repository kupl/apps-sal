# cook your dish here
n = int(input())
x = []
y = []
for _ in range(n):
    s = input().split(' ')
    x.append(int(s[0]))
    y.append(int(s[1]))
q = x[0]
w = y[0]
for t in range(n - 1):
    x[t] = (x[t] + x[t + 1]) / 2
    y[t] = (y[t] + y[t + 1]) / 2
x[n - 1] = (x[n - 1] + q) / 2
y[n - 1] = (y[n - 1] + w) / 2
i = 0
a = 0
while(i < n - 1):
    a += (x[i] * y[i + 1] - y[i] * x[i + 1]) / 2
    i += 1
a += (x[i] * y[0] - y[i] * x[0]) / 2

print(abs(a))
# print(x,y)

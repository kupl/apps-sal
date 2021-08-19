# cook your dish here
n = (int(input()))
x = []
for _ in range(n):
    a, b = map(int, input().split())
    a = [a, a + b]
    x.append(a)
x.sort()
y = -1
c = 0
for i in range(len(x)):
    if x[i][0] > y:
        c += 1
        y = x[i][1]
print(c)

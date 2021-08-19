(n, k) = list(map(int, input().split()))
x = str(n)
a = []
for i in range(len(x)):
    if k < 1:
        break
    if x[i] != '9':
        x = x[0:i] + '9' + x[i + 1:]
        k -= 1
print(x)

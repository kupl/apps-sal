n, k = map(int, input().split())
x = str(n)
j = 0
v = []
for i in range(0, len(x)):
    if x[i] == '9':
        v.append(x[i])
        continue
    else:
        if j < k:
            j = j + 1
            v.append('9')
        else:
            v.append(x[i])
print("".join(v))

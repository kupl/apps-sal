n = int(input())
s = k = 0
for i in input()[::2]:
    if i == '1':
        k += 1
    else:
        s += k
print(s)

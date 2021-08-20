n = int(input())
a = str(input())
b = str(input())
k = True
result = 0
for i in range(n):
    if a[i] == b[i]:
        if k == False:
            result += 1
        k = True
    elif k == False and z != a[i]:
        result += 1
        k = True
    elif k == False and z == a[i]:
        result += 1
    else:
        k = False
        z = a[i]
if k == False:
    result += 1
print(result)

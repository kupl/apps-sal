n = int(input())
a = list(input())
b = list(input())
other_0 = other_1 = imp_0 = imp_1 = 0
for i in range(n):
    if b[i] == '1':
        if a[i] == '0':
            other_0 += 1
        else:
            other_1 += 1
    elif a[i] == '0':
        imp_0 += 1
    else:
        imp_1 += 1
print(imp_0 * other_1 + imp_1 * other_0 + imp_0 * imp_1)

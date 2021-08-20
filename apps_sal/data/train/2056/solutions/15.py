n = int(input())
a = list(input())
b = list(input())
i = 0
num = 0
while i < n:
    if i == n - 1:
        if a[i] == b[i]:
            i += 1
        else:
            num += 1
            i += 1
    elif a[i] == b[i]:
        i += 1
    elif a[i] == '1' and a[i + 1] == '0' and (b[i] == '0') and (b[i + 1] == '1'):
        num += 1
        i += 2
    elif a[i] == '0' and a[i + 1] == '1' and (b[i] == '1') and (b[i + 1] == '0'):
        num += 1
        i += 2
    elif a[i] != b[i]:
        num += 1
        i += 1
print(num)

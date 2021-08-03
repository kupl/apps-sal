a = input()
b = a.find('0')
if b >= 0:
    print(a[:b] + a[b + 1:])
else:
    print(a[1:])

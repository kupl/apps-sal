a = input()
i0 = a.find('0')
print(a[:i0] + a[i0 + 1:] if i0 != -1 else a[1:])

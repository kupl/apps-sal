lst = input().split()
m = min(lst, key=len)
for i in range(len(lst)):
    print(m, lst[i], end=' ')
print(m)

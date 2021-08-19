x = [str(x) for x in input().split()]
y = x[:]
x.sort(key=len)
ele = x[0]
leng = len(x)
for i in range(0, leng):
    print(ele + ' ' + y[i], end=' ')
print(ele)

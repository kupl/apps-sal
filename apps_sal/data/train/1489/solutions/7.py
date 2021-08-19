num, k = input().split()
k = int(k)
# print(num)
# print(num[0])
l = []
old = ''
for x in range(len(num)):
    if num[x] != '9' and k > 0:
        old = '9'
        l.append(old)
        k = k - 1
    else:
        l.append(num[x])


for x in l:
    print(x, end='')

import copy
n = int(input())
a = list(map(int, input().split()))
c = []
for i in range(len(a)):
    if a[i] == 2:
        c.append(1)
    else:
        str = bin(a[i])[2:]
        if len(str) != 32:
            rem = 32 - len(str)
            str = '0' * rem + str
        str1 = copy.deepcopy(str)
        str1 = list((x for x in str1))
        if str[31] == '0':
            str1[31] = '0'
        if str[31] == '1':
            str1[31] = '1'
        if str[30] == '0':
            str1[30] = '1'
        if str[30] == '1':
            str1[30] = '0'
        str1 = ''.join(str1)
        x = int(str1, 2)
        c.append(x)
print(*c)

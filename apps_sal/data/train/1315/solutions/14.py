# cook your dish here
n = int(input())
dct = dict()
c = 0
for i in range(n):
    x = input()
    for j in x:
        if j.isdigit():
            if j in list(dct.keys()):
                dct[j] += 1
            else:
                dct[j] = 1
for k in dct:
    if dct[k] == 1:
        c += 1
print(c)

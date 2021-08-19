n = int(input())
a = input()
b = input()
if len(set(a)) == 1:
    print(0)
else:
    ed = 0
    zer = 0
    for i in a:
        if i == '0':
            zer += 1
        else:
            ed += 1
    sed = szer = 0
    for i in range(n):
        if b[i] == '0':
            if a[i] == '0':
                szer += 1
            else:
                sed += 1
    print(sed * zer + szer * ed - szer * sed)

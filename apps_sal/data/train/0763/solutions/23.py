def fun(a, b):
    x = 0
    y = 0
    for i in a:
        if i == '1':
            x += 1
    for i in b:
        if i == '1':
            y += 1
    flag = 0
    ones_so_far = 0
    for i in range(len(a)):
        if a[i] == '1':
            ones_so_far += 1
        if a[i] == '0' and b[i] == '1':
            if ones_so_far != x:
                flag = 1
    if x == y and flag == 0:
        print("Yes")
    else:
        print("No")


for xxx in range(int(input(''))):
    n = int(input(''))
    a = input('')
    b = input('')
    fun(a, b)

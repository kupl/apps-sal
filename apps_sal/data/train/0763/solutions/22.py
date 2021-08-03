def fun(a, b):
    if a.count('1') == b.count('1'):
        x = 0
        for i in range(len(a)):
            if a[i] == '1' and b[i] == '0':
                x = x + 1
            if a[i] == '0' and b[i] == '1':
                x = x - 1
            if x < 0:
                return 0
        if x == 0:
            return 1
        else:
            return 0
    return 0


for xxx in range(int(input(''))):
    n = int(input(''))
    a = input('')
    b = input('')
    if fun(a, b) == 1:
        print("Yes")
    else:
        print("No")

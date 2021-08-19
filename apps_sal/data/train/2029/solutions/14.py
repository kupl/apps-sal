def even(num):
    return bool(num % 2 == 0)


list = []
n = input()
n = int(n)
if even(n) == True:
    print('NO')
else:
    for i in range(1, n + 1):
        if not even(i):
            list.append(2 * i - 1)
        else:
            list.append(2 * i)
    for i in range(1, n + 1):
        if even(i):
            list.append(2 * i - 1)
        else:
            list.append(2 * i)
    print('YES')
    for x in list:
        print(x, end=' ')

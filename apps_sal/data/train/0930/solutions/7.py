tests = int(input())
for test in range(tests):
    n = int(input())
    a = [[0 for i in range(n)] for i in range(n)]
    count = 1
    for k in range(n):
        i = 0
        for j in range(k, -1, -1):
            a[i][j] = count
            count += 1
            i += 1
    for k in range(1, n):
        i = k
        j = n - 1
        for i in range(k, n):
            a[i][j] = count
            count += 1
            j -= 1
    my_str = ''
    for i in range(n):
        for j in range(n):
            my_str += str(a[i][j])
            my_str += ' '
        my_str += '\n'
    print(my_str)

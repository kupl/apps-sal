def seven(m):
    i = 0
    while(len(str(m)) > 2):
        number = [int(i) for i in str(m)]
        n = len(number)
        m = int(str(m)[:(n - 1)]) - (2 * number[n - 1])
        i = i + 1
    return (m, i)

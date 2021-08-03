def fib(n1):
    fn_1 = 1
    fn_2 = 0
    f = 0
    for i in range(1, n1):
        f = fn_1 + fn_2
        fn_2 = fn_1
        fn_1 = f
    return f


def fib_digits(n):
    check = 0
    num = ''
    l = []
    count = 0
    x = str(fib(int(n)))
    while len(x) > 1:
        for j in range(len(x)):
            if x[0] == x[j]:
                count += 1
        num += x[0]
        l.append((count, int(x[0])))
        count = 0
        x = x.replace(x[0], "")
    l.sort()
    return(l[::-1])

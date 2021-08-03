def skrzat(base, n):
    if base == "b":
        return 'From binary: {} is {}'.format(n, sum([int(j) * ((-2)**i)for i, j in enumerate(n[::-1])]))
    else:
        def do(n1):
            li = []
            while n1 != 0:
                li.append(str(abs(n1 % (-2))))
                n1 //= -2
            return li[::-1]
        return 'From decimal: {} is {}'.format(n, "".join([do(abs(n)), do(-n)][n > 0]) or 0)

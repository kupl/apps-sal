def balanced_num(number):
    b = list(str(number))
    if len(str(number)) % 2 != 0:
        i = len(str(number)) // 2
        bsum = 0
        asum = 0
        for n in b[0:i]:
            bsum += int(n)
        for n in b[-1:i:-1]:
            asum += int(n)
        if bsum == asum:
            return 'Balanced'
        else:
            return 'Not Balanced'
    else:
        i = len(str(number)) // 2
        bsum = 0
        asum = 0
        for n in b[0:i - 1]:
            bsum += int(n)
        for n in b[-1:i:-1]:
            asum += int(n)
        if bsum == asum:
            return 'Balanced'
        else:
            return 'Not Balanced'

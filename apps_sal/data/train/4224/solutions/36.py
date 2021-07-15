def dont_give_me_five(start,end):
    def has_five(n):
        x = False
        for i in str(n):
            if i == '5':
                x = True
        return x
    y = 0
    for i in range(start, end + 1):
        if not has_five(i):
            y = y + 1
    return y

def skiponacci(n):
    s = '1'
    num = 1
    prv = 0
    for i in range(1,n):
        new = num + prv
        prv = num
        num = new
        if i%2 == 0:
            s = s + ' ' + str(num)
        else:
            s += ' skip'

    return s

def series_sum(n):
    if n == 0:
        return '0.00'
    else:
        x = 1
        sum = 0
        for i in range(n):
            sum += 1/(x)
            x += 3
        
        
        s = "{:0.2f}".format(sum)
        return s


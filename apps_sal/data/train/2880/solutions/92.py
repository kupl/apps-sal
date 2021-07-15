def seven(m):
    count = 0
    
    while m > 99:
        ost = m % 10
        m = m // 10 - ost * 2
        count += 1
    
    return (m, count)

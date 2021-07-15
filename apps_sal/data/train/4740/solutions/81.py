def row_sum_odd_numbers(n):
    c = 0
    for i in range(n + 1):
        c += i
    if c > 1:
        index = 1
        a = []
        for j in range(c):
            a.append(index)
            index += 2
        s = 0
        e = c - n
        while c != e:
            s += a[c - 1]
            c -= 1
        return s
    else:
        return n
            
        
        
        


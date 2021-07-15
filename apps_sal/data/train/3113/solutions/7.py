def distribute(m, n):
    if m <=0:
        return [0]*n
    if n <= 0:
        return []
    else:
        lst = [0]*n
        x = m//n
        y = m%n
        while x > 0:
            for i in range(n):
                lst[i] += 1
            x -= 1
        if y > 0:
            for j in range(y):
                lst[j] += 1
        return lst

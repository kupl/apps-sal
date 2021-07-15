def multiples(m, n):
    arr = [] 
    start = 1
    while m >= start: 
        arr.append(start * n)
        start += 1
    return arr


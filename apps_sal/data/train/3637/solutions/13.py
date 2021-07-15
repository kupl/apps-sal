def num_primorial(n):
    i = 2
    sum = 1
    k = 0
    while True:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            sum *= i
            k += 1
        if k == n:
            break
        i += 1
    return sum 

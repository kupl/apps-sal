def consecutive_ducks(n):
    '''
    find x + (x + 1) = n thus x exists if (n-1) % 2 == 0
    if not, find x + (x + 1) + (x + 2) = n
    4*x + 1+2+3+4
    5*x + 1+2+3+4+5
    '''
    sum = 0
    for i in range(1, n // 2):
        sum += i
        if sum > n:
            continue
        if (n - sum) % (i + 1) == 0:
            return True
    return False

def odd_count(n):
    '''count = 0
    for x in range(n):
        if(x % 2 != 0):
            count += 1'''
    return len(list(range(1, n, 2)))

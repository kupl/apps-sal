def number_increasing(n):
    if n == 1:
        return True
    elif n % 5 == 0:
        return False 
    else:
        return [1,27,3,9][n%5 - 1] <= n

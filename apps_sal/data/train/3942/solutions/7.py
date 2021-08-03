def solve(n):
    counter = 0
    counter += n // 500
    n = n % 500
    counter += n // 200
    n = n % 200
    counter += n // 100
    n = n % 100
    counter += n // 50
    n = n % 50
    counter += n // 20
    n = n % 20
    counter += n // 10
    n = n % 10
    if counter < 1 or n != 0:
        return -1
    else:
        return counter

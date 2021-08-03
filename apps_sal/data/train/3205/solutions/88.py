def is_divisible(n, x, y):
    resultone = n / x
    resulttwo = n / y
    if resultone == int(resultone) and resulttwo == int(resulttwo):
        return True
    else:
        return False

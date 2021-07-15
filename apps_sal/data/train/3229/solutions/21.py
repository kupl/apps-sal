def am_i_wilson(n):
    try:
        return (factorial(n - 1) + 1) % (n * n) == 0 if n != 1 else False
    except:
        return False
    
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

def find(n):
    result = 0
    while n > 0:
        if n == 0:
            break
        elif n%3 == 0 or n%5 == 0: 
            result += n
        n-=1
    return result

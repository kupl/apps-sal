def find(n):
    x = [number for number in range(n+1) if number%3==0 or number%5==0]
    return sum(x)


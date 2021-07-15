def find(n):
    x = 0
    multiples = []
    while x <= n:
        if x % 3 == 0 or x % 5 == 0:
            multiples.append(x)
        x += 1
    return sum(multiples)

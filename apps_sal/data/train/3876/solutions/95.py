def find(n):
    multiples = []
    for i in range(1, n+1):
        if i % 5 == 0 or i % 3 == 0:
            multiples.append(i)
    return sum(multiples)


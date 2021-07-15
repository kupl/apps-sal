def solve(n):
    counter = 0
    nom = [500, 200, 100, 50, 20, 10]
    for d in nom:
        q,n = divmod(n,d)
        counter +=q
    if n : return -1
    return counter

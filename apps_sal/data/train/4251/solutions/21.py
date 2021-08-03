def difference_of_squares(n):
    s1 = 0
    for i in range(1, n + 1):
        s1 += i**2
    somme2 = [i for i in range(1, n + 1)]
    s2 = (sum(somme2))**2

    return abs(s1 - s2)

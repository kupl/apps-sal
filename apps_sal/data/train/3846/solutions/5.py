# Taking advandage of relation between the 'steps' between terms of the sequence and the sequence itself

# eg
# f2    =  1, 2, 4, 6, 10, 14, 20, 26, 36, 46, ....
# steps =  1, 2, 2, 4, 4, 6, 6, 10, 10, 14, 14, ....  each term of f2 repeated 2 times (start with 1)

# f3    =  1, 2, 3, 5, 7, 9, 12, 15, 18, 23
# steps =  1, 1, 2, 2, 2, 3, 3, 3, 5, 5, 5, ....  each term of f3 repeated 3 times (start with 1)

def f(k, n):
    fk = [*range(1, k + 1)]
    x = 2
    for i in range(k + 1, n + 2):
        fk += [fk[-1] + x]
        if i % k == 0:
            x = fk[i // k]
    return fk[n]

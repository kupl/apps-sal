def smallest_integer(matrix):
    s, n = {elt for l in matrix for elt in l}, 0
    while True:
        if n not in s:
            return n
        n += 1

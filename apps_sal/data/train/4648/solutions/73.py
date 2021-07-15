def automorphic(n):
    new_n = n**2
    n = str(n)
    new_n = str(new_n)
    if new_n[-len(n):] == n:
        return "Automorphic"
    else:
        return "Not!!"

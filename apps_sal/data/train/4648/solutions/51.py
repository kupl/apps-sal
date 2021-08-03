def automorphic(n):

    if (n**2) % 10**(len(str(n))) == n:
        return "Automorphic"
    else:
        return "Not!!"

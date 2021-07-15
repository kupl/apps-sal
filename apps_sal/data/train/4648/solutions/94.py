def automorphic(n):
    pow_n = n**2
    result = str(pow_n)[-len(str(n)):]

    return "Automorphic" if int(result) == n else "Not!!"

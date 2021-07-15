def automorphic(n):
    number = str(n**2)[-len(str(n)):]
    return "Automorphic" if number == str(n) else "Not!!"


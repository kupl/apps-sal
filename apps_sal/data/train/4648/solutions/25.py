def automorphic(n):
    s1 = str(n ** 2)
    if s1.endswith(str(n)):
        return "Automorphic"
    return "Not!!"

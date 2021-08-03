def automorphic(n):
    lth = len(str(n))
    last = str(n ** 2)[-lth:]
    if str(n) == last:
        return "Automorphic"
    else:
        return "Not!!"

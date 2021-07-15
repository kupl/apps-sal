def automorphic(n):
    x = n ** 2
    c = len(str(x))
    for i in str(n)[::-1]:
        if i != str(x)[c - 1]:
            return "Not!!"
        c -= 1
    return "Automorphic"

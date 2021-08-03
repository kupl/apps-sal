def automorphic(n):
    print(n)
    print((str(n**2)))
    print((str(n**2 - n)[-1]))
    print((str(n**2 - n)))
    if n < 10:
        if str(n**2 - n)[-1] == '0':
            print((n**2))
            return "Automorphic"
    if n > 9 and n < 100:
        if str(n**2 - n)[-1] == '0' and str(n**2 - n)[-2] == '0':
            print((n**2))
            return "Automorphic"
    if n > 100:
        if str(n**2 - n)[-1] == '0' and str(n**2 - n)[-2] and str(n**2 - n)[-3] == '0':
            print()
            print((n**2))

            return "Automorphic"

    return "Not!!"

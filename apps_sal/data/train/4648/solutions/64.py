def automorphic(number):
    data = str(number)

    res = str(number**2)
    l = len(data)

    return "Automorphic" if res[-l:] == data else "Not!!"

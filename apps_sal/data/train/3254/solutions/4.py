def any_odd(x):
    bin = "{0:b}".format(x)
    bin = bin[::-1]
    odd = 0
    print(bin)
    for letter in bin:
        if odd%2 == 1 and letter == '1':
            return 1
        odd+= 1
    return 0

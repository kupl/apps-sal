def seven(n):

    count = 0
    while n>99:
        n = int(str(n)[:-1]) - 2*int(str(n)[-1])
        count += 1

        

    return (n, count)


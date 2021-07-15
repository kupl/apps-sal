def seven(m, i = 0):
    while m>=100:
        return seven( int(str(m)[:-1]) - int(2 * int(str(m)[-1])) , i+1)
    return (m,i)


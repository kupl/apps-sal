def div(s):
    s = str(s)
    return int(s[:-1]) - 2 * int(s[-1])

def seven(m):
    counter = 0
    while m >= 100:
        m = div(m)
        counter += 1
    return (m, counter)    


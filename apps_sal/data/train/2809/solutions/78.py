def digitize(n):
    listn = []
    for x in str(n):
        listn.append(int(x))
    revl = listn[::-1]
    return revl

f = False
while f == False:
    s = input().strip()
    d = dict()
    f = True
    for i in s:
        if i in list(d.keys()):
            f = False
        else:
            d[i] = 1
    if not f:
        print("Invalid")
    else:
        print("Valid")

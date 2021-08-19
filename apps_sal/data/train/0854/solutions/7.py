ncases = int(input())

for cases in range(ncases):
    nlen = int(input())
    testlist = list(map(int, input().split()))
    if not testlist:
        continue
    # if len(testlist) != nlen:
    #    continue
    mydict = set()
    beautiful = True
    for a in testlist:
        if a not in mydict:
            mydict.add(a)
        else:
            beautiful = False
    if beautiful:
        print("prekrasnyy")
    else:
        print("ne krasivo")

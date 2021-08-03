def tidyNumber(n):
    string = str(n)
    j = 0
    # print(string)
    for i in string:
        if int(i) >= j:
            j = int(i)
            continue
        else:
            return False
    return True

def tidyNumber(n):
    cpy = n
    l = len(str(cpy))
    cpy = [int(i) for i in str(cpy)]
    for i in range(l):
        for j in range(i, l - 1):
            if cpy[j] <= cpy[j + 1]:
                continue
            else:
                return False
    return True
    # your code here
    # pass

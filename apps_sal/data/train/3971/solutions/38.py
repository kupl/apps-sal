def tidyNumber(n):
    n = str(n)
    tidy = True
    for i in range(1, len(n)):
        if int(n[i]) >= int(n[i - 1]):
            continue
        else:
            tidy = False
            break
    return tidy

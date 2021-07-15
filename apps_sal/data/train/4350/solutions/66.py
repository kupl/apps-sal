def pre_fizz(n):
    tab = []
    if n == 1:
        tab.append(1)
        return tab
    else:
        for i in range(1, n+1):
            tab.append(i)
    return tab

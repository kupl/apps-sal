def trouble(x, t):
    while(1):
        for i in range(len(x) - 1):
            if x[i] + x[i+1] == t:
                x.pop(i+1)
                break
        else:
            break
    return x

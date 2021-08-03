def find_missing_number(x):
    try:
        x = sorted(list(map(lambda i: int(i), (x.split()))))
        for i in range(1, len(x) + 1):
            if x[i - 1] != i:
                return(i)
        return(0)
    except:
        return(1)

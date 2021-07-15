def series_sum(n):
    return (str(round(1+sum(1/x for x in range(4,n*3,3)),2)) if n>1 else str(float(n))).ljust(4,"0")

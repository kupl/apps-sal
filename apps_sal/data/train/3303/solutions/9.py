def div_con(x):
    # your code here
    return sum(i for i in x if isinstance(i, int)) - sum(int(i) for i in x if isinstance(i, str))

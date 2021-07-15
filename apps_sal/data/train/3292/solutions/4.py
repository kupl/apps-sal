def calc(x):
    return sum(sum(6 for i in str(ord(i)) if i == '7') for i in x)

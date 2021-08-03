def calc(x):
    return ''.join([str(ord(x[i])) for i in range(len(x))]).count('7') * 6

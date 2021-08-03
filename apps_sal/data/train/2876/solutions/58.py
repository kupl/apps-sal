
def check(a, x):
    a = set(a)
    a = list(a)
    a.append(x)
    if len(a) == len(set(a)):
        return False
    else:
        return True

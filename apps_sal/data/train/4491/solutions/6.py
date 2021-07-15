
def solve(a,b):
    string = a+b
    return ''.join([i for i in a if i not in b] + [i for i in b if i not in a])

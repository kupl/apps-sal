import string
a = string.ascii_lowercase
def solve(arr):
    p = 0
    m = []
    for s in arr:
        if len(s) > len(a):
            s = s[:len(a)]
        for num, i in enumerate(s):
            if i.lower() == a[num]:
                p+=1
        m.append(p)
        p = 0
    return m

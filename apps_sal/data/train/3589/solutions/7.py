def next_numb(n):
    if n>9876543201:
        return "There is no possible number that fulfills those requirements"
    x=n-n%3+3
    while True:
        if x>9876543201:
            return "There is no possible number that fulfills those requirements"
        if x&1:
            a=[d for d in str(x)]
            s=list(set(a))
            if len(a)==len(s):
                return x
        x+=3

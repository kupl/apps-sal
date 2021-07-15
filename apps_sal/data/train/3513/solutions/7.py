def folding(a,b):
    if a%b==0:
        return int(a/b)
    elif a>b:
        return folding(b,a%b)+int(a/b)
    elif b>a:
        return folding(a,b%a)+int(b/a)


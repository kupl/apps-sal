def solve(s):
    y= [i for i in s[::-1] if not i.isspace()]
    for i,x in enumerate(s):
        if x==' ':
            y.insert(i,' ')
    return ''.join(y)

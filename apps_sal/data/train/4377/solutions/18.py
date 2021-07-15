def solve(a, b):
    x=0
    y=0
    for i in range(0,len(a)):
        if a[i]==b[i]:
            pass
        elif a[i]>b[i]:
            x+=1
        else:
            y+=1
    if x==y:
        return '{}, {}: that looks like a "draw"! Rock on!'.format(x,y)
    elif x>y:
        return '{}, {}: Alice made "Kurt" proud!'.format(x,y)
    else:
        return '{}, {}: Bob made "Jeff" proud!'.format(x,y)

def sierpinski(n):
    if n==1:
        return ' * \n* *'
    s=sierpinski(n-1).split('\n')
    n=len(s[0])
    r=[]
    for row in s:
        r.append(' '*((n+1)//2)+row+' '*((n+1)//2))
    for row in s:
        r.append(row+' '+row)
    return '\n'.join(r)

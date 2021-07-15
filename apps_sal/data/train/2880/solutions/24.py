def seven(m):
    z=0
    while (len(str(m)) > 2):
        x=int(str(m)[:(len(str(m))-1)])
        y= abs(m) % 10
        m=x-2*y
        z=z+1
    return (m,z)


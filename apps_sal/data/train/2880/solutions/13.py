def seven(m):
    i=0
    while len(str(m)) >=3:
        x = str(m)[:len(str(m))-1]
        z = str(m)[len(str(m))-1:]
        m = int(x) - (int(z)*2)
        i+=1
    return (m,i)

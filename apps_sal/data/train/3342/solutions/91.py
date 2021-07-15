def pattern(n):
    st = ""
    for n in range(1,n+1):
        st+= str(n)*n+"\n"
    return st[:-1]

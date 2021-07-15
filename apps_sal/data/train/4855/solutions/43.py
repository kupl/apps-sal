def vert_mirror(st):
    a = st.split("\n")
    for i in range(len(a)):
        a[i] = list(a[i])
        a[i].reverse()
        a[i] = ''.join(a[i])
    return  "\n".join(a)
def hor_mirror(st):
    a = st.split('\n')
    a.reverse()
    return "\n".join(a)
def oper(fct, s):
    return fct(s)

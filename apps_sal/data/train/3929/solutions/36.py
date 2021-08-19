def reverse(st):
    print(st)
    a = []
    for x in reversed(st.split()):
        print(x)
        a.append(x)
    return ' '.join(a)

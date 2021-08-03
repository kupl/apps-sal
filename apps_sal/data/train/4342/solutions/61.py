def no_space(x):
    c = []
    for i in range(len(x)):
        c. append(x[i])
    while ' ' in c:
        c. remove(' ')

    return ''. join(c)

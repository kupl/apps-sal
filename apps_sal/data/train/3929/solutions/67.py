def reverse(st):
    x = st.split(' ')
    y = []
    for i in range(len(x) - 1, -1, -1):
        if x[i]:
            y.append(x[i])
    return ' '.join(y)

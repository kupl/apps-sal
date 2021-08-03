def increment_string(foo):
    index = -1
    for i in range(len(foo) - 1, -1, -1):
        if not foo[i] in '0123456789':
            break
        index = i

    if index == -1:
        foo = foo + '1'
    else:
        a = len(foo[index:])
        foo = foo[:index] + ("{:0>" + str(a) + "d}").format(int(foo[index:]) + 1)

    return(foo)

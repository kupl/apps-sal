""" 1) LOOP CAT ? """


def read_out(array):
    acrostic = ''
    for word in array:
        acrostic += word[0]
    return acrostic


' 2) LIST COMP ? '


def read_out(a):
    return ''.join((w[0] for w in a))


' 3) MAP OBJ ? '


def read_out(a):
    return ''.join([w[0] for w in a])

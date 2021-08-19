def two_sort(array):
    temp = array.sort()
    new = array[0]
    out = ''
    for i in range(len(new) - 1):
        out += new[i] + '***'
    out += new[-1]
    return out

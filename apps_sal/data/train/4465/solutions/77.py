def super_size(n):
    temp = [int(x) for x in str(n)]
    temp.sort(reverse=True)
    strings = [str(integer) for integer in temp]
    a_string = "".join(strings)
    an_integer = int(a_string)
    return an_integer

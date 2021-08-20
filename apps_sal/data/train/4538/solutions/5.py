def reverse_fun(n):
    string = ''
    for i in range(len(n)):
        string += n[::-1][0]
        n = n[::-1][1:]
    return string

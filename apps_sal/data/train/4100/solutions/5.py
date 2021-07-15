def reverse_alternate(string):
    string = string.split()
    res = []
    for i in range(len(string)):
        if (i+1) % 2 == 0:
            res.append(string[i][::-1])
        else :
            res.append(string[i])
    return " ".join(res)


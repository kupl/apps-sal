def solution(string):
    if string == None:
        return("")
    else:
        x = string[::-1]
    return("{}".format(x))

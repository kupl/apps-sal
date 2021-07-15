def solution(*args):
    print  (args)
    result = {}
    for x in args:
        if x in result:
            return True
        else :
            result[x] = 1
    return False


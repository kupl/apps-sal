def string_constructing(pattern, target):
    pattern = list(pattern)
    target = list(target) + [None]
    buffer = [None]
    pos = 0
    count = 0
    while (True):

        if(target[pos] == buffer[pos]):
            if(target[pos] == None):
                return count
            pos += 1
        else:
            if(buffer[pos] == None):
                buffer[-1:-1] = pattern
                count += 1
            else:
                del buffer[pos]
                count += 1

    return count

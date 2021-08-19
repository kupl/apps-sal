def esrever(string):
    if len(string) <= 1:
        return string
    return string[-2::-1] + string[-1]

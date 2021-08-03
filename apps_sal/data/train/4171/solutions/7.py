def no_repeat(string):
    # your code here
    return min(string, key=string.count)

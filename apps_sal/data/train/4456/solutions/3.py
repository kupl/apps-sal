# boo for this kata
def flatten_me(a):
    result = []
    for i in a:
        if isinstance(i, list):
            result += flatten_me(i)
        else:
            result.append(i)
    return result

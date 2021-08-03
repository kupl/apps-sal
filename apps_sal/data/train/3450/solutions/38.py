def array(string):
    res = string.split(',')
    if len(res) < 3:
        return None
    res.pop()
    res.pop(0)

    return ' '.join(res)

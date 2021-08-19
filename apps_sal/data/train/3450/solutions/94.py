def array(string):
    new_string = string.split(',')
    results = ''
    for i in range(len(new_string)):
        if i != 0 and i != len(new_string) - 1:
            results += new_string[i] + ' '
    if not len(results):
        return None
    return results[0:-1]

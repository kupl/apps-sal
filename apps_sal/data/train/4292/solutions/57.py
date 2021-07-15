def string_clean(s):
    output = ''
    for x in s:
        print(x.isdigit())
        if x.isdigit():
            pass
        else:
            output += x
    return output

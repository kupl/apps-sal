from re import sub


def calculate(input):
    try:
        return eval(sub('([^\\d])0+(\\d)', '\\1\\2', input))
    except:
        return False

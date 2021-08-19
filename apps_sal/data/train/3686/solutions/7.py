from re import sub


def calculate(s):
    try:
        return eval(sub('\\b0+(?=\\d)', '', s))
    except:
        return 0

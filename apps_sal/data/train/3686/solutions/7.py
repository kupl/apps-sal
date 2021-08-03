from re import sub


def calculate(s):
    try:
        return eval(sub(r'\b0+(?=\d)', '', s))
    except:
        return 0

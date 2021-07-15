from re import sub

def calculate(input):
    try:
        return eval(sub(r'([^\d])0+(\d)', r'\1\2', input))
    except:
        return False

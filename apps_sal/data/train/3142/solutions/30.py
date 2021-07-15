from re import sub

def seven_ate9(str):
    return sub(r'79(?=7)', '7', str)

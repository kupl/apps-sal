from re import sub


def seven_ate9(str):
    return sub('79(?=7)', '7', str)

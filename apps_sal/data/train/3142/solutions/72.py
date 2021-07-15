import re

def seven_ate9(num):
    return re.sub("(?<=7)(9)(?=7)", "", num)

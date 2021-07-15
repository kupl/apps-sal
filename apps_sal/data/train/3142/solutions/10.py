import re

def seven_ate9(s):
    return re.sub(r'(?<=7)9(?=7)', '', s)

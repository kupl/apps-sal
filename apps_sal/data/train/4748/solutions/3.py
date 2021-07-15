import re
def insert_dash2(num):
    s = re.sub(r'([2468])(?=[2468])',r'\1*',str(num))
    return re.sub(r'([13579])(?=[13579])',r'\1-',s)


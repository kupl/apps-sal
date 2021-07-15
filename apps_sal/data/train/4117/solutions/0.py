import re
def sum_from_string(string):
    d = re.findall("\d+",string)
    return sum(int(i) for i in d)

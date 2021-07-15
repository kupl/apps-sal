import re
def kooka_counter(stri):
    stri = re.sub(r"H+","H",stri.replace("a",""))
    stri = re.sub(r"h+","h",stri.replace("a",""))
    return len(stri)

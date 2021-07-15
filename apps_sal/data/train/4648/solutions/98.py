import re
def automorphic(n):
    reg = re.compile(r'.*%s$' % n)
    if reg.search(str(n * n)) != None:
        return "Automorphic"
    return "Not!!"

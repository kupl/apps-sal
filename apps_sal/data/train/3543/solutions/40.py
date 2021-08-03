import re
def increment_string(i): return (lambda x: i + '1' if x == None else i[:i.index(x.group(0))] + str(int(x.group(0)) + 1).zfill(len(x.group(0))))(re.search("\d+$", i))

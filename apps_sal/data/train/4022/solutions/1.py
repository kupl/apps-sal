import re
def soundex(name):
    newNameLis = [x[0].upper()+x.lower() for x in name.split(" ")]
    newNameLis = [x[0] + x[1]+x[2:].translate(str.maketrans('', '','hw')) for x in newNameLis]
    newNameLis = [x[0] + x[1:].translate(str.maketrans('bfpvcgjkqsxzdtlmnr', '111122222222334556','')) for x in newNameLis]
    newNameLis = [x[0] + re.sub(r'(\d)\1*', r'\1',x[1:]) for x in newNameLis]
    newNameLis = [x[0] + x[1]+x[2:].translate(str.maketrans('', '','aeiouy')) for x in newNameLis]
    newNameLis = [x[0] + "".join([i for i in x[2:] if i.isdigit()]) for x in newNameLis]
    return " ".join([(x+'000')[:4] for x in newNameLis])



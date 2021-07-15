from itertools import product
from string import ascii_uppercase as ap
import re
transo = list(map(lambda x:"".join(x),list(ap)+list(product(ap,repeat=2))+list(product(ap,repeat=3))+list(product(ap,repeat=4))))
def spreadsheet(no):
    matches = re.match(r"(?P<RC1>^R\d+C\d+$)|(?P<A1>^(?P<LET>[A-Z]+)\d+$)",no)
    if matches.group("RC1"):
        asi = matches.group("RC1")
        asiind = asi.index("C")
        return transo[int(asi[asiind+1:])-1] + asi[1:asiind]
    else:
        asi = matches.group("LET")
        df = transo.index(asi)
        return f"R{no[no.rfind(asi)+len(asi):]}C{df+1}"

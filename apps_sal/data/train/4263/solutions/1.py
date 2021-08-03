import re
def apparently(Q): return re.sub(r'(?<=\band|\bbut)\b(?! apparently\b)', ' apparently', Q)

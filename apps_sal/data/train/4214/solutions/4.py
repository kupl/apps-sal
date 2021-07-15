import re
W = lambda Q : ''.join(reversed(Q)) if 6 < len(Q) and ',' != Q[-1] or 1 < Q.upper().count('T') else '0' if 1 == len(Q) else Q.upper() if 2 == len(Q) or ',' == Q[-1] else Q
spin_solve = lambda Q : re.sub('[\w\'-]{1,6},|[\w\'-]+',lambda S : W(S.group()),Q)

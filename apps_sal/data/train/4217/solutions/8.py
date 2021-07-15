from calendar import month_abbr as abr
from datetime import *

def solve(a,b):
    ans = [abr[m] for y in range(a,b+1) for m in (1,3,5,7,8,10,12) if date(y, m, 1).weekday() == 4]
    return (ans[0], ans[-1], len(ans))

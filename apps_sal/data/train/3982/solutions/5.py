from datetime import timedelta as d
from statistics import mean, median
def stat(s):
    if not s:return ''
    li = [sum(int(j) * k for j, k in zip(i.split("|"), [3600, 60, 1])) for i in s.split(", ")]
    A = lambda x: "|".join([i.zfill(2) for i in x.split(":")])[:8]
    return f"Range: {A(str(d(seconds=max(li) - min(li))))} Average: {A(str(d(seconds=mean(li))))} Median: {A(str(d(seconds=median(li))))}"

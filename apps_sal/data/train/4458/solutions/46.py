import re

def fmt(t):
    t = f"{t}"
    return t if len(t) == 2 else "0"+t

def time_correct(t):
    if t is None: return None
    if t == "": return ""
    if not re.fullmatch(r"\d{2}:\d{2}:\d{2}", t): return None
    s = sum(int(x)*(60**i) for i,x in enumerate(t.split(":")[::-1]))
    h,m,s = s//3600%24, s//60%60, s%60
    return f"{fmt(h)}:{fmt(m)}:{fmt(s)}"

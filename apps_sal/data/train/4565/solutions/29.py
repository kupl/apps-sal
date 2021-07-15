import re
def replace_dots(s):
    if len(s) == 0: return ""
    if "." in s:
        return s.replace(".","-")
    else: return s

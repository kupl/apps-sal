import re
def wheres_wally(s):
    try:
        return [m.start() for m in
                re.finditer("(?<=\s)Wally(\s|[.,\';+-]|\Z)|(?<=^)Wally(\s|[.,\';+-]|\Z)",
                            s)][0]
    except:
        return -1


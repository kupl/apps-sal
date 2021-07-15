import re

def string_expansion(stg):
    result = ""
    for match in re.finditer(r"\d*(^|\d)([^\d]+)", stg):
        count = int(match.group(1) or 1) 
        for char in match.group(2):
            result = f"{result}{count * char}"
    return result


# one-liner
#string_expansion = lambda s: "".join(f"{int(m.group(1) or 1) * c}" for m in re.finditer(r"\d*(^|\d)([^\d]+)", s) for c in m.group(2))


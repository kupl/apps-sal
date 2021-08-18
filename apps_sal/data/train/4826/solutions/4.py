import re

p = re.compile(r"[a-z][{0}][{0}]0[{0}][{0}]0[{0}][{0}][a-z]".format(re.escape("| }; &


def count_robots(a):
    n=m=0
    for x in map(str.lower, a):
        y=len(p.findall(x))
        if "automatik" in x:
            n += y
        elif "mechanik" in x:
            m += y
    return [f"{n} robots functioning automatik", f"{m} robots dancing mechanik"]

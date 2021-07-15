from functools import cmp_to_key

def meeting(s):
    def comp(a, b):
        if a[1] == b[1]:
            return -1 if a[0] < b[0] else 1
        else:
            return -1 if a[1] < b[1] else 1
    w = map(lambda x : x.split(":"), s.upper().split(";"))
    u = sorted(w, key = cmp_to_key(comp))
    return "".join(map(lambda a : "(" + a[1] + ", " + a[0] + ")", u))

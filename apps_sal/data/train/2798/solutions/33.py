def to_alternating_case(string):
    x = list(string)
    c = ""
    for k in x:
        if k == k.upper():
            c += k.lower()
        elif k == k.lower():
            c += k.upper()
        else:
            c += k
    return c

    # your code here

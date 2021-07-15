from re import findall

def derivative(eq):
    monos = ["{}", "{}x", "{}x^{}"]

    res = ""
    for t in findall("(\+|-)?(\d+)?x(?:\^(\d+))?", eq):
        a, b = (int(x) if x else 1 for x in t[1:])
        res += t[0] + monos[(b>1) + (b>2)].format(a*b, b-1)
    
    return res if res else "0"

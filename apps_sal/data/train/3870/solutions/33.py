def solve(s):
    inds = [i for i,c in enumerate(s) if c == " "]
    res = s.replace(" ","")[::-1]
    for i in inds:
        res = res[:i] + " " + res[i:]
    return res

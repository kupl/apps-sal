import re
from string import Template


def whoIsWinner(moves, con, sz):
    z = (sz + 1)**2
    r = ["-"] * z
    d = dict()
    reg = Template("(\\w)(((.{$s1}\\1){$c})|(\\1{$c})|((.{$s2}\\1){$c})|((.{$s3}\\1){$c}))")
    reg = re.compile((reg.substitute(s1=str(sz - 1), c=str(con - 1), s2=str(sz), s3=str(sz + 1))))
    for i, x in enumerate(list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")[:sz]):
        d[x] = z - (sz + 1) + i
    for s in moves:
        r[d[s[0]]] = s[2]
        d[s[0]] -= sz + 1
        m = reg.findall(("").join(r))
        if(m):
            return m[0][0]
    return "Draw"

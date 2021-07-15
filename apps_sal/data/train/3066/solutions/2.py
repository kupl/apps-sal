def negafy(s):
    res,i = "",0
    while True:
          if i == len(s): break
          if 96 < ord(s[i]) and ord(s[i]) < 123:
                res += s[:i] + "-" + s[i]
                s,i = s[i+1:],-1
          i += 1
    return res + s
def solve(s):
    while s[0] == '(' and s[-1] == ')': s = s[1:-1]
    while "--" in s: s = s.replace("--","+")
    while "+-" in s: s = s.replace("+-","-")
    while s.startswith("+"): s = s[1:]
    if "(" not in s: return s
    a = s.rindex("(")
    b,c,d = s[a:].index(")") + a,s[a-1],""
    while a > 0 and b < len(s) - 1 and s[a-1] == '(' and s[b+1] == ')':
        a,b = a-1,b+1
    if c == '-': d = negafy(s[a:b+1])
    else: d = s[a-1] + s[a+1:b]
    return solve(s[:a-1] + d + s[b+1:])

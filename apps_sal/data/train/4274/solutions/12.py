from itertools import cycle
def do_math(s) :
    op=cycle('+-*/')
    ss=s.split()
    ss=sorted(ss,key=lambda x:[i for i in x if i.isalpha()])
    ss=[int(''.join((i for i in j if i.isdigit()))) for j in ss]
    ans=ss[0]
    print(ss)
    for i in ss[1:]:
        ans = eval(str(ans)+next(op)+str(i))
    return round(ans)

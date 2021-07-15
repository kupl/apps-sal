def triangle(s):
    d = {'R':{'R':'R','G':'B','B':'G'},'G':{'R':'B','G':'G','B':'R'},'B':{'R':'G','G':'R','B':'B'}}
    for i in range(len(s)-1,0,-1):
        s = [d[s[j]][s[j+1]] for j in range(i)]
    return s[0]

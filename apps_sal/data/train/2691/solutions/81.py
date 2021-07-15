def solve(s):
    s=s+'d'
    t=[]
    d=''
    for i in range(len(s)-1):
        if s[i].isdigit():
            d=d+s[i]
            if s[i+1].isalpha():
                t.append(int(d))
                d=''
    return max(t)



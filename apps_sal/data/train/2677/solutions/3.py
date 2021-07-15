def navigate(s,e):
    a = 'abcde123fghij456klmno789pqrst.@0uvwxyz_/*&'
    d = {i: [a.index(i)//8, a.index(i)%8] for i in a}
    x=0
    y=0
    i=0
    j=0
    rowdis=0
    coldis=0
    for k,v in d.items():
        if k == s:
            i = v[0]
            j = v[1]
        if k == e:
            x = v[0]
            y = v[1]
        if abs(i-x) > 2.5:
            if i<x:
                rowdis = 6+i-x
            else : rowdis = 6-i+x
        else : rowdis = abs(i-x)
        if abs(j-y) > 3.5:
            if j<y:
                coldis = 8+j-y
            else : coldis = 8-j+y
        else : coldis = abs(j-y)
    return rowdis + coldis
def tv_remote(word):
    ans = 0
    cursor = 'a'
    shift = False
    for c in word:
        if c.isspace():        
            ans += navigate(cursor,'&') + 1
            cursor = '&'
            continue
        if c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if c.isupper():
                if not shift:
                    ans += navigate(cursor,'*') + 1
                    shift = True
                    cursor = '*'
            if c.islower():
                if shift:
                    ans += navigate(cursor,'*') + 1
                    shift = False
                    cursor = '*'
        ans += navigate(cursor,c.lower()) + 1
        cursor = c.lower()
    return ans

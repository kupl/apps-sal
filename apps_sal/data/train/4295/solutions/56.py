def balanced_num(number):
    print(number) 
    s = str(number)
    ln = len(s)//2
    if len(s)%2==1:
        l = s[:ln]
        r = s[ln+1:]
    else:
        l = s[:ln-1]
        r = s[ln+1:]
    print(("l= ",l, "r= ",r))
    res = sum([int(x) for x in l]) == sum([int(x) for x in r])

    if res:
        return 'Balanced'
    else:
        return 'Not Balanced'


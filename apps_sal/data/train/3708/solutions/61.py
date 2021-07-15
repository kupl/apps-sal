def hex_to_dec(s):
    print(s)
    v=0
    step=0
    for i in range(len(s)-1,-1,-1):
        if s[i]=='a':
            v=v+10*(16**step)
            
        elif s[i]=='b':
            v+=11*(16**step)
        elif s[i]=='c':
            v+=12*(16**step)
        elif s[i]=='d':
            v+=13*(16**step)
        elif s[i]=='e':
            v+=14*(16**step)
        elif s[i]=='f':
            v+=15*(16**step)
        else:
            v+=(int(s[i]))*(16**step)
        step+=1
    return v


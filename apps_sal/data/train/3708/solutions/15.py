def hex_to_dec(s):
    ans = 0
    dict={
        'a':10,
        'b':11,
        'c':12,
        'd':13,
        'e':14,
        'f':15
    }
    i = len(s)
    if(i == 1):
        if(s.isnumeric()):
            ans+=int(s)
        elif(s.isalpha()):
            for x,y in dict.items():
                if s == x:
                    ans+=y
    else:
        for s in s:         
            if(s.isnumeric()):
                ans += int(s)*pow(16,i-1)
                i-=1
            else:
                for x,y in dict.items():
                    if s == x:
                        ans += y*pow(16,i-1)
                        i-=1
    return ans

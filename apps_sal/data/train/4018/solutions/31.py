def isDigit(string):
    ans = True
    cd = 0
    if string == "":return False
    if string[0] == "-":
        string=string[1:]
    for i in string:
        if i == ".":
            if cd >= 1: ans=False
            else: 
                cd+=1
        else:
            try: int(i)
            except: 
                ans=False
    return(ans)


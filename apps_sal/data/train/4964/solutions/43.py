def is_uppercase(inp):
    uppers = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    lowers = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    x = 0
    
    for case in lowers:
        if case in inp:
            x+=1
    if x != 0:
        return False
    else:
        return True
            


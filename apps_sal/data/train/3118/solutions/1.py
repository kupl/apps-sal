def is_lucky(n):
    sume=0
    for i in str(n):
        sume+=int(i)
    return True if sume%9==0 else False     

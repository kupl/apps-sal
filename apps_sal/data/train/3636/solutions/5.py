def bouncy_ratio(percent):
    b=0
    n=1
    while(True):
        s=list(str(n))
        if s!=sorted(s) and s!=sorted(s)[::-1]:
            b+=1
        if float(b)/n>=percent:
            break
        n+=1
    return n

def is_divisible_by_6(s):
    out=[]
    for digit in "0123456789":
        div=int(s.replace("*",digit))
        if div%6==0:out.append(str(div))
    return out

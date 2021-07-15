def automorphic(n):
    #your code here
    strnum = str(n)
    lenstr = len(strnum)
    strnumsqr = str((n*n))
    if strnumsqr.endswith(strnum):
        return "Automorphic"
    else:
        return "Not!!"

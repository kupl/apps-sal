def solve(s):
    mas2=['0','1','2','3','4','5','6','7','8','9']
    mas=[]
    k=''
    for i in range(len(s)):
        if s[i] in mas2:
            k=k+s[i]
            if i == len(s)-1:
                mas.append(int(k))
        else:
            if k!='':
                mas.append(int(k))
                k=''
    return max(mas)

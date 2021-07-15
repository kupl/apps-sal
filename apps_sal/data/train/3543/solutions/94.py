def increment_string(strng):
    print(strng)
    n=strng
    m=[]
    x = ""
    z2=''
    r=[]
    r2=''
    y = ["0", "1", "2", "3", "4", "5", "6","7", "8", "9"]
    if n=="":
        x="1"
    else:
        for i in n:
            m.append(i)
        if m[-1] not in y:
            x=n+"1"
        else:
            m.reverse()
            for j in m:
                if j in y:
                    r.append(j)
                else:
                    break
            r.reverse()
            for j1 in r:
                r2=r2+j1
            z1=m[(len(r2)):]
            z1.reverse()
            for j2 in z1:
                z2=z2+j2
            s2 = int(r2)
            s21 = str(s2)
            s = int(r2) + 1
            s1 = str(s)
            if len(r2)==len(s21):
                x=z2+s1
            else:
                s3=r2[0:(len(r2)-len(s21))]
                s4=r2[0:(len(r2)-len(s21)-1)]
                if len(s21)==len(s1) :
                    x=z2+s3+s1
                else:
                    x=z2+s4+s1

    return x

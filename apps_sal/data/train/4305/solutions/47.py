def order_weight(strng):
    s=strng.split()
    s2=[]
    s3=[]
    order=[]
    Out=[]
    s4=""
    for i in range(len(s)):
        s2.append(int(s[i]))
        a=0
        for j in range(len(s[i])):
            a=a+s2[i]//(10**j)%10
        s3.append(a) 

    for j in range(len(s3)-1):
        for m in range(len(s3)-1):
            buf=0
            buf2=0
            if (s3[m]>s3[m+1]):
                buf=s3[m]
                s3[m]=s3[m+1]
                s3[m+1]=buf
                buf2=s2[m]
                s2[m]=s2[m+1]
                s2[m+1]=buf2
            else:
                if (s3[m]==s3[m+1]):
                    if str(s2[m])>str(s2[m+1]):
                        buf2=s2[m]
                        s2[m]=s2[m+1]
                        s2[m+1]=buf2

    for m in range(len(s2)):
        s4=s4+str(s2[m])+" "
    s5=""
    for j in range(len(s4)-1):
        s5=s5+s4[j]
    return s5


def penalty(a_list):
    for i in range(len(a_list)):
        for j in range(i+1,len(a_list)):
            a,b = a_list[i],a_list[j]
            if int(a+b) >= int(b+a):
                a_list[i],a_list[j] = b,a
    s = ""
    for k in a_list:
        s += k
    return s

def get_real_floor(n):
    if n<1:
        return n
    ls=[]
    for i in range(1,n+1):
        if i==13:
            pass
        else:
            ls.append(i)
    return ls.index(n)  #I solved this Kata on  8/21/2019  11:07 PM...#Hussam'sCodingDiary

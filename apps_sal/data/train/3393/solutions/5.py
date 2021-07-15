def list_squared(m, n):
    list=[]
    for i in range(m,n+1):
        sum=0
        s_list=[]
        for j in range(1,int(i**.5)+1):
            if i%j==0:
                div=i//j
                sum+=j**2
                if j!=div:
                    sum+=div**2
        sqt=sum**.5
        if int(sqt)==sqt:
            s_list=[i,sum]
            list.append(s_list)
    return list

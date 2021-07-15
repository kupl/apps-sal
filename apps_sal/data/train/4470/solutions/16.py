def nb_year(y,e,a,r,s=0):
    while y<r:y+=y*e*.01+a;s+=1
    return s

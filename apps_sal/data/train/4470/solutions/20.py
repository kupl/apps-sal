def nb_year(p0, percent, aug, p):
    pop=p0
    y=0
    while pop<p:pop*=(1+percent/100);pop+=aug;y+=1
    return y


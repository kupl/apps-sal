an, jh = [1], [0]
for i in range(1,int(1e5*5)):
    jh.append(i-an[jh[-1]])
    an.append(i-jh[an[-1]])
john=lambda n:jh[:n]
ann=lambda n:an[:n]
sum_john=lambda n:sum(jh[:n])
sum_ann=lambda n:sum(an[:n])

three_amigos=lambda a:min([[max(a[i:i+3])-min(a[i:i+3]),a[i:i+3]]for i in range(len(a)-2)if all(j&1==a[i]&1for j in a[i:i+3])],key=lambda x:x[0],default=[[],[]])[1]

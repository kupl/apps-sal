def split_exp(n):
    return [y.ljust(len(x)-j,'0') if i==0 else '.'+y.zfill(j+1) for i,x in enumerate(n.split('.')) for j,y in enumerate(x) if y!='0']

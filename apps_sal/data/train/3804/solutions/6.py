d = {**{0:0,1:1},**{i+1:sum(k ** (i - k + 1) for k in range(1, i))+i for i in range(2, 1000)}}
def min_length_num(dn, n): 
    for k,l in d.items():
        if k > n : return [0,-1]
        if len(str(l)) == dn : return [1,k]
    return [0,-1]

child=lambda b1,b2:0<sum([i!=j for i,j in zip(b1,b2)])<3
grandchild=lambda b1,b2:sum([i!=j for i,j in zip(b1,b2)])<5and b1+b2 not in['WB','BW']

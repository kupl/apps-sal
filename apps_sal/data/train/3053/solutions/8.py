close_compare = lambda a,b,m=0: 0 if abs(a-b)<=m else -1*(a<b)+(a>b) 

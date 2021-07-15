q,diagonal=lambda x:(x==0)*2+(x>0),lambda m:["Secondary Diagonal win!","Principal Diagonal win!",'Draw!'][q(sum(x[y]-x[::-1][y] for y,x in enumerate(m)))]


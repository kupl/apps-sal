jumping_number=lambda n:['Not!!','Jumping!!'][all(abs(ord(a)-ord(b))==1for a,b in zip(str(n),str(n)[1:]))]

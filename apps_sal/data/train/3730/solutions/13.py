capitalize=lambda s,f=lambda s,p:''.join(e if i%2==p else e.upper()for i,e in enumerate(s)):[f(s,1),f(s,0)]

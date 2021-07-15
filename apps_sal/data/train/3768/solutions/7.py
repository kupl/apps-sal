name_file=lambda f,n,s:[f.replace('<index_no>', str(i)) for i in range(s,s+n)] if n>0 and (type(n),type(s))==(int,int) else []

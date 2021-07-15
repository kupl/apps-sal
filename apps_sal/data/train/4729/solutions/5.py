numbers_of_letters=f=lambda n,N=["zero","one","two","three","four","five","six","seven","eight","nine"]:(lambda s:[s]+f(len(s))if len(s)!=n else[s])(''.join(N[i]for i in map(int,str(n))))

mormons=lambda a,r,t,m=0:m if a>=t else mormons(a*(r+1),r,t,m+1)

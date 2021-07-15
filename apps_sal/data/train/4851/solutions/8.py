sort_ranks=lambda li,A=lambda li:max(li,key=lambda x:(int(x.split(".")[0]),x)).split(".")[0]:sum([sorted([k for k in li if k.split(".")[0]==str(i)])for i in range(1,int(A(li))+1)],[])

christmas_tree=lambda n:'\r\n'.join([(n//3-j+1)*' '+(2*j+1)*'*'for i in range(n//3)for j in range(i,i+3)]+[n//3*' '+3*'#']*(n//3>0))

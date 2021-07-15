# cook your dish here
import sys

try:
    
    def readstring():
        return sys.stdin.readline().lstrip().rstrip()
        
    count=0
    ind=""
    beg=0
    
    n=readstring()
    n+="0"
    
    x1=int(n[0])
    
    for i in range(1,len(n)):
    	if n[i-1]>=n[i]:
    		if count<x1:
    			count=x1
    			ind="{}-{}".format(beg+1,i)
    		beg=i
    		x1=int(n[i])
    	else:
    		x1+=int(n[i])
    
    sys.stdout.write(str(count)+":"+str(ind)+"\n")
    
except:
    pass

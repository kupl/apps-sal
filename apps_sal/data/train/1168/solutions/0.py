import sys
for _ in range(0,eval(input())):   
    d,inp,mp,n,q=set(),list(map(ord,list(sys.stdin.readline().strip()))),[x=='b' for x in list(sys.stdin.readline().strip())],eval(input()),ord('a')
    inps = [inp[i:] for i in range(len(inp))]
    inps.sort()
    op,prev= 0,''
    for ip in inps:
        	i,ct=0,0
        	while i < min(len(ip),len(prev)):
        		if prev[i] != ip[i]:
        			break
        		if mp[ip[i]-q]:
        			ct = ct+  1
        		i = i+1
        	while i < len(ip):
        		if mp[ip[i]-q]:
        			ct = ct + 1
        		if ct > n:
        			break
        		op,i= op+1,i+1
        	prev = ip
    print(op)

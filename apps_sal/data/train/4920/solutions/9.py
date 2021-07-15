def min_special_mult(arr):  #just simple "straight forward"...
    narr=[]; l=[]; c=0 
    for a in arr:
       if a==None: continue
       if isinstance(a,int): narr.append(a)
       else:
          try:
             if int(a)==a: narr.append(a); continue
          except:
             l.append(a); c+=1 
    if c==1: return "There is 1 invalid entry: "+l[0]
    if c>0: return "There are "+str(c)+" invalid entries: "+str(l)
    narr.sort(); n=narr[-1]; n1=n
    while True:
       f=0
       for a in reversed(narr):
          if n%a!=0: f=1; break
       if f==0: return n
       n+=n1

def bubble(l):
    r=[]
    for i in range(0,len(l)):
       for j in range(1,len(l)):
          if l[j]<l[j-1]: t=l[j]; l[j]=l[j-1]; l[j-1]=t; r.append(l[:])
    return r

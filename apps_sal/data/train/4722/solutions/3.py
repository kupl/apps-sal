def e(i):
 c=i.find(')')
 if c>0:o=i[:c].rfind('(');return e(i[:o]+"{:.9f}".format(e(i[o+1:c]))+i[c+1:])
 v='';r=0;p='+'
 for s in i+p:
  if s in "+-*/" and v:w=float(v);r={'+':r+w,"-":r-w,"*":r*w,"/":r/w}[p];v='';p=s
  else:v+=s
 return r

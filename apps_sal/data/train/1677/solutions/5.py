# cook your dish here
n = int(input())
a = list(map(int,input().strip().split()))
b = list(map(int,input().strip().split()))

p = [b[0]]
c = []
d = []
for i in range(1,n):
    p.append(p[i-1]+b[i])
for i in range(n):
    c.append(a[i]-p[i])
    d.append(a[i]+p[i-1])

e = c.index(max(c))
l = c.index(max(c[1:]))
m = d.index(max(d[:n-1]))
f = d.index(max(d))
k = d.index(max(d[1:]))
g = -10000000000
h = -10000000000
if(len(d[1:e])!=0):
    g = c[l]+ max(d[1:l]) + p[n-1]
if(len(c[k+1:])!=0):
    h = d[k] + max(c[k+1:]) + p[n-1]

s1 = max(g,h,max(c[1:])+a[0]+p[n-1])
h = -10000000000
g = d[k]+max(c[:k])
if(len(d[e+1:])!=0):
    h = c[e]+max(d[e+1:])
s2 = max(g,h)
print(max(max(a),s1,s2))


    
    
#maxa = a[n-1]
#for i in range(n-1):
 #   maxa = max(a[i],maxa)
  #  for j in range(i+1,n):
   #     ssumi = a[i] + a[j]
    #    if(j - i == 1):
     #       if(i>=1):
      #          ssumi += max(0,p[n-1]+p[i-1]-p[j])
       #     else:
        #        ssumi += max(0,p[n-1]-p[j])
        #else:
         #   if(i>=1):
          #      ssumi += max(p[j-1]-p[i],p[n-1]- p[j]+ p[i-1])
           # else:
            #    ssumi += max(p[j-1]-p[i],p[n-1]- p[j])
        #print(i,j,ssumi)
        #if(ssum < ssumi):
         #   ssum = ssumi
#print(max(ssum,maxa),maxa)

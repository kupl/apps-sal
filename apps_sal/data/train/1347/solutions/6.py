x=input().split()
n=int(x[0])
m=int(x[1])
y=input().split()
fr_post=dict()
n_post=dict()
for i in range(0,m):
 z=input().split()
 if(z[0] in y):
  fr_post[int(z[1])]=z[2]
 else:
  n_post[int(z[1])]=z[2]

for key in sorted(fr_post,reverse=True):
 print(fr_post[key])
for key in sorted(n_post,reverse=True):
 print(n_post[key])


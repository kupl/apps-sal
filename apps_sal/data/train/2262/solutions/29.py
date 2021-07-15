# coding: utf-8
# Your code here!
import sys
read = sys.stdin.read
readline = sys.stdin.readline

h,w,n, *xyxy = list(map(int,read().split()))

def f(x,y):
    if y==0: return x
    elif x==h: return h+y
    elif y==w: return h+w+h-x
    else: return h+w+h+w-y    

m = iter(xyxy)
res = []
idx = 0
for x1,y1,x2,y2 in zip(m,m,m,m):
    if (x1*(h-x1)==0 or y1*(w-y1)==0) and (x2*(h-x2)==0 or y2*(w-y2)==0):
        res.append((f(x1,y1),idx))
        res.append((f(x2,y2),idx))
        idx += 1


res.sort()
#print(res)

st = []
for d,i in res:
    if st and st[-1] == i:
        st.pop()
    else:
        st.append(i)

if st:
    print("NO")
else:
    print("YES")











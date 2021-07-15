# cook your dish here
from operator import itemgetter
inp=list(map(int, input().split()))
n, m, w, b = inp[:4]
stops=[]
for i in range(w):
 stops.append((inp[4+2*i]-1,inp[5+2*i]-1,'w'))
for i in range(b):
 stops.append((inp[4+2*w+2*i]-1,inp[5+2*w+2*i]-1,'b'))
stops.sort(key=itemgetter(1))
stops.sort(key=itemgetter(0))
counter=0
stop_rows=[[] for _ in range(n)]
for stop in stops:
 stop_rows[stop[0]].append(stop[1:])
for row in stop_rows:
 idx=0
 for i in range(len(row)):
  if idx==row[i][0]:
   idx+=1
  else:
   if row[i][1]=='w':
    if i<len(row)-1:
     num=row[i+1][0]-idx+1
     counter+=((num*(num+1))>>1)-1
     idx=row[i][0]+1
     num=row[i+1][0]-row[i][0]+1
     counter-=((num*(num+1))>>1)-1
    else:
     num=m-idx
     counter+=((num*(num+1))>>1)-1
     idx=row[i][0]+1
     num=m-row[i][0]
     counter-=((num*(num+1))>>1)-1
   else:
    num=row[i][0]-idx+1
    counter+=((num*(num+1))>>1)-1
    idx=row[i][0]+1
 num=m-idx
 counter+=(num*(num+1))>>1
print(counter)


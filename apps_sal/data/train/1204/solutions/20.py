# cook your dish here
import sys
input = sys.stdin.readlines
print = sys.stdout.write
t = input()
for case in range(1,int(t[0])*2,2):
 s = t[case]
 r = t[case+1]
 unlike = []
 curr=None
 l = 0
 k = 0
 for i in range(len(s)-1):
  if r[i]!=s[i]:
   l += 1
   if curr:
    unlike.append(curr)
    k+=1
   curr = 0
  else:
   if curr!=None:
    curr += 1
 k += 1
 unlike.sort()
 mini = k*l
 for i,j in enumerate(unlike):
  k-=1
  l+=j
  mini = min(mini,k*l)
 print(str(mini)+'\n')

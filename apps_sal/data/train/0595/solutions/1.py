import sys,math
from sys import stdin,stdout


s=stdin.readline().strip()

ispalin=[[0 for i in range(len(s)+1)] for i in range(len(s)+1)]
suff=[[-1 for i in range(len(s)+1)] for i in range(len(s)+1)]
pref=[[-1 for i in range(len(s)+1)] for i in range(len(s)+1)]
lcp=[[0 for i in range(len(s)+1)] for i in range(len(s)+1)]

for i in range(0,len(s)):
 ispalin[i][i]=1;pref[i][i]=1;suff[i][i]=1
 ispalin[i][i+1]=1;pref[i][i+1]=2;suff[i][i+1]=2

#for i in ispalin:
 #print(i)

for l in range(2,len(s)+1):
 for i in range(0,len(s)-l+1):
  #print(i,i+l-1,s[i],s[i+l-1])
  ispalin[i][i+l]=ispalin[i+1][i+l-1]*int(s[i]==s[i+l-1])
  pref[i][i+l]=pref[i][i+l-1]+ispalin[i][i+l]
  suff[i][i+l]=suff[i+1][i+l]+ispalin[i][i+l]

for i in range(len(s)):
 for j in range(i+1,len(s)):
  lcp[i][j]=(lcp[i-1][j+1]+1)*int(s[i]==s[j])

#

ans=0

for i in range(1,len(s)):
 for j in range(i,len(s)):
  #if lcp[i-1][j]!=0:
  #print(i,j,lcp[i-1][j],suff[i][j],pref[i][j],s[0:i],s[i:j],s[j:])
  ans+=(lcp[i-1][j]*(suff[i][j]+pref[i][j]-1))
#
stdout.write(str(ans))




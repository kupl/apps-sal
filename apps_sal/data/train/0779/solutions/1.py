test=int(input())
for i in range(test):
 N=int(input())
 n=input()
 a=list(n.split(' '))
 for k in range(N):
  a[k]=int(a[k])
 a.sort(reverse=True)
 sum= a[0]/(2**(N-1))
 for j in range(1,N):
  sum+= a[j]/(2**(N-j))
 print(sum)
 


# cook your dish here
t=int(input())
rr=[]
for i in range(t):
 n=int(input())
 s=input()
 s=list(s)
 s.sort()
 rr.append(s[0])
for i in rr:
 print(i)

import sys 
input = sys.stdin.readline
yes = "YES"
no = "NO"
s=input()
t=input()
ls=[0]
lt=[0]
p=0
for c in s:
    if c == "A":p += 1
    else:p-= 1
    ls.append(p)
p=0
for c in t:
    if c == "A":p += 1
    else:p-= 1
    lt.append(p)

q=int(input())
for _ in range(q):
    a,b,c,d = map(int,input().split())
    if (ls[b]-ls[a-1])%3 == (lt[d]-lt[c-1])%3:print(yes)
    else:print(no)

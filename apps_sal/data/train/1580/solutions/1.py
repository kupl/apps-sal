n= int(input())
s1=''
for _ in range(n):
    s=input()
    s1=s1+s
s1=s1.lower()
s1=s1.replace('.','').replace(',','').replace("'","").replace(':','').replace(';','')
a=set(s1.split())
b=list(a)
b.sort()
print(len(b))
for i in b:
    print(i)


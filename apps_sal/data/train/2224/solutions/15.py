a,b,c,d=0,0,0,0
n=int(input())
s1,s2=input(),input()

for i in range(n):
    a+=s1[i]=='0' and s2[i]=='1'
    b+=s1[i]=='0' and s2[i]=='0'
    c+=s1[i]=='1' and s2[i]=='1'
    d+=s1[i]=='1' and s2[i]=='0'

print(a*d+b*c+b*d)


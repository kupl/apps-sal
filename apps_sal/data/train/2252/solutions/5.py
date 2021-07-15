n = int(input())
string_count = {}
for _ in range(n):
    s = str(input())
    item_count={}
    for i,c in enumerate(s):
        item_count[c]=item_count.get(c,0)+1
    s0=[]
    for i,x in enumerate('abcdefghijklmnopqrstuvwxyz'):
        if item_count.get(x,0)%2==1:
            s0.append(x)
    s1 = ''.join(s0)
    string_count[s1]=string_count.get(s1,0)+1
points=0
for j,a in enumerate(string_count):
    x = string_count[a]
    points+=x*(x-1)//2
    for i in range(len(a)):
        points+=x*string_count.get(a[:i]+a[i+1:],0)
print(points)

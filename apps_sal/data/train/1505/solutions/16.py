# cook your dish here
# cook your dish here
l = int(input())
a = list(map(int, input().split()))
stack = []
p, md, d = 0, 0, 0
mp, ml, l = 0, 0, 0
mpIndex = 0

for i in range(len(a)):
    if(d == 0):
        l = 0
        mpIndex = i+1
        
    l += 1
    
    if(a[i] == 1):
        d+=1
    else:
        d-=1
    
    if(d > md):
        md = d
        p = i+1
    
    if(l > ml):
        ml = l
        mp = mpIndex

print(md, p, ml, mp)

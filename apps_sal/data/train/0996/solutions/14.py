# cook your dish here
t = int(input())
l1 = []
l2 =[]
p1 =0
p2 = 0
for _ in range(t):
    n,m= map(int,input().split())
    p1+=n
    p2+=m    
    if p1 > p2:
       l = p1-p2
       l1.append(l)
       l2.append(0)
    else:
        l = p2 -p1
        l1.append(0)
        l2.append(l)
w1 =max(l1)
w2 = max(l2)
if w1 > w2:
    print('1',w1,sep = ' ')
else:
    print('2',w2,sep = ' ')
        

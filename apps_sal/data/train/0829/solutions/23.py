n = int(input())
l = list(map(int,input().split()))
l.sort()
c,sum = 0,0
for i in l:
    if c < len(l):
        c+=1 
        for x in l[c:]:
            sum = sum + abs(i-x)

print(sum)


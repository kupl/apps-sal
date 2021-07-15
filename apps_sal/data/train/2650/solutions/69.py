n, l = map(int,input().split())
lw=[]
for i in range(n):
    lw.append(input())
lw.sort()
print("".join(lw))

n,k=map(int, input().split())
ids=[]
pr=list(map(int, input().split()))
pr.pop(0)
relatives=[]

def common_member(a, b): 
    a_set = set(a) 
    b_set = set(b) 
    return len(a_set.intersection(b_set))

for _ in range(n-1):
    ids.append(list(map(int, input().split())))
for i in ids:
    i.pop(0)

for i in ids:
    if common_member(pr,i)>=k:
        relatives.append(i)
        ids.remove(i)
y=1
while y>=0:
    y=0
    for x in relatives:
        for i in ids:
            if common_member(x,i)>=k:
                relatives.append(i)
                ids.remove(i)
                y+=1
    if y==0:
        y=-1

print(len(relatives)+1)

# cook your dish here
def find_relatives(list1):
    global graph,relatives,K
    temp={}
    for j in list1:
        if j not in graph:
            list1.remove(j)
    for i in range(len(list1)):
        temp1 = graph[list1[i]]
        for j in temp1:
            try:
                temp[j] +=1
            except:
                temp[j]=1
    keys = list(temp.keys())
    rel1=[]
    for j in range(len(keys)):
        if temp[keys[j]] >=K:
            if keys[j] not in relatives:
                rel1.append(keys[j])
    return rel1
from collections import defaultdict
N,K = map(int,input().split())
listim=list(map(int,input().split()))
listim = listim[1:]
listcit=[]
for i in range(N-1):
    temp = list(map(int,input().split()))
    temp= temp[1:]
    listcit.append(temp)
graph= defaultdict(list)
for i in range(len(listcit)):
    for x in listcit[i]:
        graph[x].append(i)
relatives=[]
t1 = find_relatives(listim)
rel = t1
for j in rel:
    relatives.append(j)
while len(rel)!=0:
    for i in rel:
        t1 = find_relatives(listcit[i])
        rel = t1
        for j in rel:
            relatives.append(j)
print(len(relatives)+1)

    

import re

n = int(input())
arr = []
ans = []

for i in range(n):
    temp = input().lower().split()
    for j in temp:
        valids = re.sub(r"[^a-z]+", '', j)
        arr.append(valids)

while('' in arr):
    arr.remove('')

'''for j in range(len(temp)):
        if(temp[j]=='.' or temp[j]==';' or temp[j]=='\'' or temp[j]==':'):
            del(temp[j])
        if(temp[j]==',' or temp[j]=="\n" or temp[j]==""):
            del(temp[j])
        
    for j in range(len(temp)):
        arr.append(temp[j])'''
ans = arr
'''for i in arr:
    valids = re.sub(r"[^a-z]+", '', i)
    ans.append(valids)
    print(ans)'''

ans = list(set(list(ans)))
ans.sort()
print(len(ans))
print(*ans, sep='\n')

import re
n = int(input())
arr = []
ans = []
for i in range(n):
    temp = input().lower().split()
    for j in temp:
        valids = re.sub('[^a-z]+', '', j)
        arr.append(valids)
while '' in arr:
    arr.remove('')
'for j in range(len(temp)):\n        if(temp[j]==\'.\' or temp[j]==\';\' or temp[j]==\'\'\' or temp[j]==\':\'):\n            del(temp[j])\n        if(temp[j]==\',\' or temp[j]=="\n" or temp[j]==""):\n            del(temp[j])\n        \n    for j in range(len(temp)):\n        arr.append(temp[j])'
ans = arr
'for i in arr:\n    valids = re.sub(r"[^a-z]+", \'\', i)\n    ans.append(valids)\n    print(ans)'
ans = list(set(list(ans)))
ans.sort()
print(len(ans))
print(*ans, sep='\n')

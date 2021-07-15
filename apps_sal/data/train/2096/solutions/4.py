def binSearch(arr, el):
    if len(arr) == 0: return -1
    l, p = 0, len(arr)-1
    while l != p:
        s = (l+p) // 2
        if arr[s] < el:
            l = s + 1
        else:
            p = s
    return l if arr[l] == el else -1

n = int(input())
a = [int(i) for i in input().split()]
s = sorted(a)

subsList = []
visited = [False for i in range(n)]
for i in range(n):
    ind = i
    newSub = False
    while not visited[ind]:
        if not newSub:
            subsList.append([])
        newSub = True
        visited[ind] = True
        subsList[-1].append(str(ind+1))
        ind = binSearch(s, a[ind])
    
out = str(len(subsList)) + "\n"
for lineNr in range(len(subsList)-1):
    
    out += str(len(subsList[lineNr])) + " "
    out += " ".join(subsList[lineNr]) + "\n"
out += str(len(subsList[-1])) + " "    
out += " ".join(subsList[-1])
print(out)
        



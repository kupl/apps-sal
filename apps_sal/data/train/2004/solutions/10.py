import sys

l = sys.stdin.readline()

sz = len(l) - 1
temp = []

c = 0
for i in range(sz):
    if(l[i] == "0"):
        c = i
        break
    temp.append(l[i])
    
if(c == 0):
    print(l[1:])
    return
else:    
    for i in range(c + 1, sz):
        temp.append(l[i])
    
print("".join(temp))

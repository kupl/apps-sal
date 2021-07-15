import sys

s = input()

num = len(s)

if s[-1] == "1" or s[0] == "0":
    print((-1))
    return

s = s[:-1]

for i in range(num // 2):
    
    if s[i] != s[-1-i]:
        print((-1))
        return

lis = []
ans = []

for i in range(num-1):

    if i != 0 and s[i] == "1":
        lis.append(i+1)

#print (lis)

now = 1
for i in range(len(lis)):

    while now < lis[i]:
        ans.append([now,lis[i]])
        now += 1

    if i != len(lis)-1:
        ans.append([lis[i],lis[i+1]])
        now += 1

ans.append([num-1,num])


for i in ans:
    print((i[0],i[1]))


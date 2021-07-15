from sys import stdin
n, q = tuple(int(x) for x in stdin.readline().split())

tpl = tuple(x for x in stdin.readline().split())

dic = {}
amt = {}
for i in range(n):
    dic[tpl[i]] = i
    if tpl[i] not in amt:
        amt[tpl[i]] = 1
    else:
        amt[tpl[i]] += 1

ans = 0
counter = 0
while counter < n:
    right_bound = dic[tpl[counter]]
    involved = set((tpl[counter],))
    counter += 1
    while counter < right_bound:
        if tpl[counter] not in involved:
            involved.add(tpl[counter])
            right_bound = max(right_bound, dic[tpl[counter]])
        counter += 1
    
    
    temp = tuple(amt[x] for x in involved)
    ans += sum(temp) - max(temp)
print(ans)


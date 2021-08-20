n = int(input())
s = input()
s = s.split()
d = {}
flag = 'No'
(two, four) = (0, 0)
for i in s:
    if i in d:
        d[i] += 1
        if d[i] == 2:
            two += 1
        elif d[i] == 4:
            four += 1
    else:
        d[i] = 1
d = {}
if two > 1 or four > 0:
    flag = 'Yes'
else:
    for i in range(n - 1):
        ex = int(s[i]) ^ int(s[i + 1])
        if ex in d:
            d[ex].append(i)
            if d[ex][-1] - d[ex][0] > 1:
                flag = 'Yes'
                break
        else:
            d[ex] = [i]
print(flag)

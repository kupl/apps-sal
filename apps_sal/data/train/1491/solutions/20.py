import itertools
(a, b, c, d) = list(map(float, input().split()))
li = list(itertools.permutations([a, b, c, d]))
flag = False
for i in li:
    if i[0] / i[1] == i[2] / i[3]:
        flag = True
        break
if flag == True:
    print('Possible')
else:
    print('Impossible')

t = int(input())
ml = []
nl = []
test = set(['9'])

for i in range(t):
    m,n = [int(x) for x in input().split(' ')]
    if set(list(str(n))) == test:
        nl.append(len(str(n)))
    else:
        nl.append(len(str(n))-1)
    ml.append(m)

for i in range(len(ml)):
    if nl[i]==0:
        print('0 0')
    else:
        print(ml[i]*nl[i],ml[i])



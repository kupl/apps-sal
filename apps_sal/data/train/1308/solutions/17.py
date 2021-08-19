import collections
while True:
    list1 = []
    c = input()
    flag = 1
    flag2 = 0
    d = collections.Counter(c)
    for x in list(d.keys()):
        if d[x] > 1:
            flag = 0
            break
    temp1 = sum([d[x] for x in list(d.keys()) if x.isalpha()])
    temp2 = sum([d[x] for x in list(d.keys()) if x.isdigit()])
    if flag and temp1 and temp2:
        print('Valid')
        break
    else:
        print('Invalid')

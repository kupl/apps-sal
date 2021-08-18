for i in range(int(input())):
    s = input()
    s1 = set(s)
    l = []
    for j in s1:
        l.append(s.count(j))
    if(max(l) >= 2):
        print('yes')
    else:
        print('no')

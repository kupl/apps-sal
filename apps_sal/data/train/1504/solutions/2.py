t = int(input())
while t>0:
    t-=1
    n = int(input())
    s = input().strip()
    previ = s[0]
    num = 0
    _s = []
    dic = {}
    for i in s:
     if previ == i:
      num+=1
      continue
     _s.append((previ, num))
     if previ not in dic or dic[previ]<num:
      dic[previ] = num
     #l.append(previ)
     previ = i
     num  = 1
    _s.append((previ, num))
    if previ not in dic or dic[previ]<num:
      dic[previ] = num

    ##print(_s)
    sum1 = sum(dic.values())
    del dic, s

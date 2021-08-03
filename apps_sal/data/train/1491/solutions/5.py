a, b, c, d = list(map(float, input().split()))
li = []
li.append(a)
li.append(b)
li.append(c)
li.append(d)
li = sorted(li)
if li[1] / li[0] == li[3] / li[2]:
    print("Possible")
else:
    print("Impossible")

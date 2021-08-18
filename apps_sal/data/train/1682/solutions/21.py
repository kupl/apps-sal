l = list(input())
s = int(l[0])
l1 = []
l2 = []
l3 = []
l3.append(1)
for i in range(1, len(l)):
    if int(l[i - 1]) < int(l[i]):
        s += int(l[i])
    else:
        l1.append(int(s))
        s = int(l[i])
        l3.append(i + 1)
    if i == len(l) - 1:
        l3.append(i + 1)
        l1.append(int(s))
'''print(max(l1),l1,l3)
if l3[1 + l1.index(max(l1))] == len(l):
    print("{}:{}-{}".format(max(l1), l3[l1.index(max(l1))], l3[1 + l1.index(max(l1))]))
else:
    print("{}:{}-{}".format(max(l1), l3[l1.index(max(l1))], l3[1 + l1.index(max(l1))] - 1))

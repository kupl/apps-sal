li = list(map(int, input().split()))
li = sorted(li)
a, b, c, d = li
# print float(b/float(a))
# print float(d/float(c))
if float(b / float(a)) == float(d / float(c)):
    print("Possible")
else:
    print("Impossible")

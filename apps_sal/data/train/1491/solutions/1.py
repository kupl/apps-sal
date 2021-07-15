a = input().split()
a = [int(x) for x in a]
a.sort()
if (float(a[0])/float(a[1]))==(float(a[2])/float(a[3])):
 print("Possible")
else:
 print("Impossible")

a, b = [int(x) for x in input().split()]
r = list(str(a-b))
if r[0] == "1":
 r[0] = "2"
else:
 r[0]="1"
print("".join(r))


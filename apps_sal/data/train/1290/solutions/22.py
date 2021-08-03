n = int(input())
s = str(n)
l = list(s)
x = 0
if len(l) > 3:
    print("More than 3 digits")
else:
    for i in l:
        x += 1
    print(x)

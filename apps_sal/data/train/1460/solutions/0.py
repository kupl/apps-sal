# cook your dish here

l = [int(k) for k in input().split()]
s = [int(k) for k in input().split()]
x = l[1] * l[0]
for i in range(l[0]):
    if(s[i] == 1):
        x += l[2]
    elif(s[i] == 2):
        x += (l[2] * 98 / 100)
    elif(s[i] == 3):
        x += (l[2] * 96 / 100)
    elif(s[i] == 4):
        x += (l[2] * 94 / 100)
    elif(s[i] == 5):
        x += (l[2] * 92 / 100)
    elif(s[i] == 6):
        x += (l[2] * 90 / 100)
if(x >= 300):
    print("YES")
else:
    print("NO")

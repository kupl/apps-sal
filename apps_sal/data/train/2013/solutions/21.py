import sys
a = list(input())
b = ""
l = 0
o = 0
for x in range (len(a)):

    if a[x] == 'a' and l == 1:
        break
    elif a[x] != 'a':
        a[x] = chr(ord(a[x])-1)
        l = 1
        o = 1

if o == 0:
    a[len(a)-1] = "z"
print("".join(a))

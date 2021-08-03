n = int(input())
li = []
for i in range(n):
    a = input().split(" ")
    l = []
    for i in a:
        l.append(int(i))
    a, b = l[0], l[1]
    if a < b:
        li.append("<")
    elif a > b:
        li.append(">")
    else:
        li.append("=")
for i in li:
    print(i)

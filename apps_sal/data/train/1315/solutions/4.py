# cook your dish here
l = []
for i in range(int(input())):
    t = list(set(list(map(int, input().split()))))
    if t not in l:
        l.append(t)
    else:
        l.remove(t)
print(len(l))

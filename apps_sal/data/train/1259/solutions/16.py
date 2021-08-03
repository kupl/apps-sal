# cook your dish here
x = int(input())

lst = []

for i in range(0, x):
    l, r = input().split()
    l = int(l)
    r = int(r)
    sublst = []
    while l <= r:
        if l % 10 == 2 or l % 10 == 3 or l % 10 == 9:
            sublst.append(l)
        l += 1
    lst.append(len(sublst))

for i in range(0, x):
    print(lst[i])

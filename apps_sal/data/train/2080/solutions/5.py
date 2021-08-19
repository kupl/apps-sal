input()
d = [int(i) for i in input().split()]
c = int(input())
b = [int(i) for i in input().split()]
b.sort()
# d.sort()
take = 1
p = min(d)
s = 0
buy = p
for i in reversed(b):
    if buy:
        s += i
        buy -= 1
    else:
        if take:
            take -= 1
        else:
            buy = p
            take = 1

print(s)

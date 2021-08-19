i = 0
l = []
while i < 10 ** 3:
    l.append(i * (i + 1) / 2)
    i = i + 1
t = int(input())
for _ in range(t):
    x = int(input())
    for i in range(1, len(l)):
        if x == l[i]:
            print(i)
        elif x < l[i] and x > l[i - 1]:
            print(i - 1)
        else:
            pass

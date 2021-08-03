l = []
for _ in range(int(input())):
    l.append(int(input()))
for i in range(2, max(l)):
    r = [x % i for x in l]
    if len(set([x % i for x in l])) == 1:
        print(i, end=' ')

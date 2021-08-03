s = input()
l = s.split()
a = 1000000000000000000
smallest = 'z' * 100000000
for i in range(0, len(l)):
    if len(l[i]) < a:
        smallest = l[i]
        a = len(l[i])
ll = []
for i in range(len(l)):
    print(smallest, end=' ')
    print(l[i], end=' ')
print(smallest, end='')

n = int(input())

a = sorted(zip(list(map(int, input().split())), list(range(n))))

s = []

for i in range(n):

    if a[i]:

        l = []

        s.append(l)

        while a[i]:

            l.append(i + 1)

            a[i], i = None, a[i][1]


print(len(s))

for l in s:

    print(len(l), *l)

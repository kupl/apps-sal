# cook your dish here
a = input()
a = [int(i) for i in a]
l = []
for i in range(len(a)):
    s = a[i]
    k = 0
    for j in range(i, len(a) - 1):
        if a[j] < a[j + 1]:
            s += a[j + 1]
            k += 1
        else:
            break
    l.append([i + 1, k + 1 + i, s])
for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i][-1] > l[j][-1]:
            c = l[i]
            l[i] = l[j]
            l[j] = c
print("{}:{}-{}".format(l[-1][-1], l[-1][0], l[-1][1]))

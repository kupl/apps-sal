# cook your dish here
n = int(input())
l = [1]
ind = 0
for i in range(n):
    t = int(input())
    if len(l) >= t:
        print(l[t - 1])
    else:
        while len(l) < t:
            l += [l[ind] * 6, l[ind] * 6 + 1]
            ind += 1
        print(l[t - 1])

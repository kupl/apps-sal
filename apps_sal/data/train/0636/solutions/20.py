# cook your dish here
x = list(map(int, input().split()))
n = x[0]
t = x[1]
a = x[2:n + 2]
count = 0
for i in range(3, n, 1):
    for j in range(2, i, 1):
        for k in range(1, j, 1):
            for l in range(k):
                #print(a[i] + a[j] + a[k] + a[l])
                if a[i] + a[j] + a[k] + a[l] == t:
                    #print(a[i] + a[j] + a[k] + a[l])
                    count += 1
print(count)

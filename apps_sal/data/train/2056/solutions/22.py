n = int(input().strip())
a = input().strip()
b = input().strip()
a = [x for x in a]
b = [x for x in b]
sum = 0
li = []
dict = {}
for k in range(n):
    if (a[k] != b[k]):
        li.append(k)
        dict[k] = int(a[k])
if (len(li) == 0):
    print(0)
elif (len(li) == 1):
    print(1)
else:
    sum = 0
    int
    k = 0
    while (k < len(li) - 1):
        if (dict[li[k]] != dict[li[k + 1]]):
            if (li[k + 1] - li[k] > 1):
                sum = sum + 1
                k = k + 1
            else:
                sum = sum + 1
                k = k + 2
        else:
            sum = sum + 1
            k = k + 1
    if(k == len(li) - 1):
        sum = sum + 1
    print(sum)

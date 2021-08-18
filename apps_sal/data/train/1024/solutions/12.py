t = int(input())

sum1 = 0
list2 = list()
list3 = list()
list4 = list()

while t > 0:
    s, n, k, r = input().split()
    s = int(s)
    list3.append(s)
    n = int(n)
    k = int(k)
    r = int(r)
    list1 = []
    sum1 = s + sum1
    ans = k
    while n > 0:
        list1.append(ans)
        ans = ans * r
        n -= 1
    m = sum(list1)
    list2.append(m)
    z = s - m
    list4.append(z)
    t -= 1
x = sum(list2)

for i in list4:
    if i > 0:
        print('POSSIBLE', i)
    else:
        print('IMPOSSIBLE', -i)


if x > sum1:
    print('IMPOSSIBLE')
else:
    print('POSSIBLE')

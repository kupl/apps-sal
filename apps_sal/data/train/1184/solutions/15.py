# cook your dish here
from collections import Counter
ans = ""
sum = 0
for _ in range(int(input())):
    n = int(input())
    x = {"A": 0, "B": 0, "C": 0, "D": 0}
    price = 0
    li = []
    for i in range(0, n):
        a = tuple(map(str, input().split()))
        li.append(a)
    # print(li)
    z = Counter(li)
    # print(z.most_common())
    cost = 100
    for y in z.most_common():
        if(x[y[0][0]] == 0):
            # print(y[0][0])
            x[y[0][0]] = 1
            # print(y[1])
            #print(int(y[1]) * cost)
            price += int(y[1]) * cost
            cost -= 25
    for p in list(x.values()):
        if(p == 0):
            price -= 100
    ans += str(price) + "\n"
    sum += price
print(ans, sum)

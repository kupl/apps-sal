t = eval(input())
li = [0] * 100001
li[1] = 1
for j in range(2, 100001):
    li[j] = li[j - 1] * j % 1589540031
for x in range(t):
    n = eval(input())
    print(li[n])

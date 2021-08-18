t = int(input())
for i in range(t):
    l = list(map(int, input().split(' ')))
    a = l[0]
    b = l[1]

    l1 = list(map(int, input().split(' ')))
    for i in range(b):
        l2 = list(map(int, input().split(' ')))
        a1 = l2[0]
        b1 = l2[1]
        print(sum(l1[a1 - 1:b1]))

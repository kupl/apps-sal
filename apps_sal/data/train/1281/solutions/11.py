relist = [1, 2, 3, 4, 5, 6, 7]
t = int(input())
for i in range(t):
    a = int(input())
    list1 = list(map(int, input().split()))
    newlist = []
    revlist = list1[::-1]
    for i in list1:
        if i not in newlist:
            newlist.append(i)
    if newlist == relist and list1 == revlist:
        print('yes')
    else:
        print('no')

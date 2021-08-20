a = int(input())
for i in range(a):
    b = str(input()).split(' ')
    li = [0] * int(b[0])
    for j in range(int(b[0])):
        li[j] += j + 1
    if int(b[0]) == int(b[1]) + 1:
        print(*li)
    else:
        li.sort()
        li.remove(int(b[0]))
        li.remove(int(b[1]) + 1)
        li.insert(int(b[1]), int(b[0]))
        li.insert(int(b[0]) - 1, int(b[1]) + 1)
        print(*li)

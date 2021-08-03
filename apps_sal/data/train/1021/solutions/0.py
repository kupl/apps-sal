class Node:
    def __init__(self, x):
        self.x = x
        self.next = None
        self.prev = None
        self.flag = True


for t in range(1):
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n):
        arr[i] = Node(arr[i])
    for i in arr:
        d = [i.x % 3 == 0, i.x, i.x // 3, i.x * 2]
        if d[0]:
            for j in arr:
                if j.x == d[2]:
                    i.next = j
                    j.prev = i
                    break
            else:
                for j in arr:
                    if j.x == d[3]:
                        i.next = j
                        j.prev = i
                        break
        else:
            for j in arr:
                if j.x == d[3]:
                    i.next = j
                    j.prev = i
                    break
    f, l = None, None
    for i in arr:
        if i.prev == None:
            f = i
        elif i.next == None:
            l = i
    while f != l and l != None:
        print(f.x, end=" ")
        f = f.next
    print(f.x)

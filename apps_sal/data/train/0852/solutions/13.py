for _ in range(int(input())):
    k = int(input())
    s = ""
    count = 1
    for i in range(k):
        for j in range(k):
            if count == 0:
                count = 1
            else:
                count = 0
            s += str(count)
        print(s)
        s = ""
        if k % 2 == 0:
            if count == 0:
                count = 1
            else:
                count = 0

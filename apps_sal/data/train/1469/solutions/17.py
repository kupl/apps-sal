for _ in range(int(input())):
    k = int(input())
    count = 2
    s = ""
    for i in range(k):
        for j in range(k):
            s += str(count + j)
        print(s)
        s = ""
        count += 1

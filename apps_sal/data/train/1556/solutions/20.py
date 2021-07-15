# cook your dish here
for _ in range(int(input())):
    k = int(input())
    s = ""
    count = 1
    for i in range(k):
        for j in range(k):
            s += str(count)
            if count == 1:
                count = 0
            else:
                count = 1
        print(s)
        s = ""
        count = 1

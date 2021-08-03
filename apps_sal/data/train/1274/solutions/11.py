n = int(input())
s = ""
for i in range(n):
    a = int(input())
    k = 1
    for j in range(1, a + 1):
        while(k < a + 1):
            s = s + str(k) + str(j)
            k = k + 1
        print(s)
        s = ""
        k = 1

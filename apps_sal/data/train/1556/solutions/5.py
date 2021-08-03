# cook your dish here
for i in range(int(input())):
    k = int(input())
    m1 = k
    c = 1
    z = 0
    count = 0
    while(k > 1):
        if(z % 2 == 0):
            c = c * 10
        else:
            c = c * 10 + 1
        k -= 1
        z += 1
    for j in range(m1):
        print(c)

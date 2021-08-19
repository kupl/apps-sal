# cook your dish here
t = int(input())
for i in range(t):
    s = 0
    n = int(input())
    l = [100, 50, 10, 5, 2, 1]
    k = n
    while(k != 0):
        for j in range(len(l)):
            s = s + (k // l[j])
            k = k % l[j]
        print(s)

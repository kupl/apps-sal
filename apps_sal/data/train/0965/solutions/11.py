# cook your dish here
for i in range(int(input())):
    n, k = map(int, input().split())
    if(k != 0):
        s = n // k
        t = n % k
        print(s, t)
    elif(k == 0):
        print(0, n)

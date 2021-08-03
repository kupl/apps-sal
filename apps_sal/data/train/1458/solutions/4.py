# cook your dish here
for i in range(int(input())):
    a = 0
    n = int(input())
    while(n > 0):
        a += n * n
        n = n - 2
    print(a)

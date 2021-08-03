# cook your dish here
n = int(input())
for i in range(n):
    x = int(input())

    # res=0
    # for j in range(1,x+1):
    #     res+=(j*j)
    print((x * (x + 1) * (2 * x + 1)) // 6)

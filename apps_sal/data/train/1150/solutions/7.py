# cook your dish here
T = int(input())
for i in range(0, T):
    N = int(input())
    count = 0
    while N != 0:
        N = N - (((N**0.5) // 1)**2)
        count += 1
    print(count)

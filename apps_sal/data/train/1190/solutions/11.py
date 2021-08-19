# cook your dish here
t = int(input())
l = [2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
for _ in range(t):
    c = 0
    n = int(input())
    i = 0
    while n:
        c += n // l[i]
        n = n % l[i]
        i = i + 1
    print(c)

# cook your dish here
for _ in range(int(input())):
    k = int(input())
    # n=k-1
    a = k * (k + 1)
    a = a / 2
    a = a**2
    print(int((2 * a) - (k**3)))

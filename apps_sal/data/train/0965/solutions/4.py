# cook your dish here
for x in range(int(input())):
    n, k = input().strip(' ').split()
    n = int(n)
    k = int(k)
    if k == 0:
        print(0, n)
    else:
        n = int(n)
        k = int(k)
        print(n // k, n % k)

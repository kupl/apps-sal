# cook your dish here
for t in range(int(input())):
    n, k = [int(x)for x in input().rstrip().split()]
    d = [int(x)for x in input().rstrip().split()]
    for i in range(0, n):
        if d[i] % k == 0:
            print("1", end="")
        else:
            print("0", end="")
    print("\r")

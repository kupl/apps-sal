# cook your dish here
for _ in range(int(input())):
    k, n = map(str, input().split())
    if k[0] == k[1] == k[2]:
        print(1)
    elif k[0] != k[1] and k[0] != k[2] and k[1] != k[2]:
        print(27)
    else:
        print(8)

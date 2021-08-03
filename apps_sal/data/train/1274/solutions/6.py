# cook your dish here
for u in range(int(input().strip())):
    n = int(input().strip())
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # print('{0}{1}'.format(j,i))
            print('{0}{1}'.format(j, i), end="")
        print()

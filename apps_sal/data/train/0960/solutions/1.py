# cook your dish here
for _ in range(int(input())):
    k = int(input())
    x = 1
    for i in range(k):
        for j in range(k):
            print('{0:b}'.format(x), end=' ')
            x = x + 1
        print()

# cook your dish here
for _ in range(int(input())):
    k = int(input())
    x = 2
    for i in range(k):
        for j in range(k):
            print(x, end='')
            x = x + 2
        print()

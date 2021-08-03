# cook your dish here

for _ in range(int(input())):
    k = int(input())
    for i in range(k):
        print('*' * i, end='')
        for j in range(k - i, 0, -1):
            print(j, end="")
        print()

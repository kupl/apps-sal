for _ in range(int(input())):
    k = int(input())
    for i in range(k):
        for j in range(k):
            print(j + 1, end='')
            print(i + 1, end='')
        print()

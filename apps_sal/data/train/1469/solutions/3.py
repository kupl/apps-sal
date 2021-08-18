for i in range(int(input())):
    k = int(input())
    count = 2
    for j in range(k):
        count = 2 + j
        for l in range(k):
            print(count, end='')
            count += 1
        print()

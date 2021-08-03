for i in range(int(input())):
    k = int(input())
    count = 1
    for j in range(1, k + 1):
        for l in range(1, k + 1):
            print(count * 2, end="")
            count += 1
        print()

for _ in range(int(input())):
    n = int(input())
    for i in range((n + 1) // 2):
        for j in range(i):
            print(end=" ")
        print("*\r")

    for i in range((n // 2) - 1, -1, -1):
        for j in range(i):
            print(end=" ")
        print("*\r")

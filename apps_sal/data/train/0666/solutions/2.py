try:
    for _ in range(int(input())):
        k = int(input())
        num = 1
        for i in range(1, k + 1, 1):
            for j in range(1, k + 1, 1):
                print(num, end="")
                num = num + 1
            print("")
except:
    pass

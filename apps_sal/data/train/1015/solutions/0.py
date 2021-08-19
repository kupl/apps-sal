# cook your dish here
try:
    for _ in range(int(input())):
        k = int(input())
        num = 1
        for i in range(1, k + 1, 1):
            for j in range(1, k + 1, 1):
                print(num * 2, end="")
                num = num + 1
            print("")
except:
    pass

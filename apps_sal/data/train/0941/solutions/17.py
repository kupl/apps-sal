try:
    for i in range(int(input())):
        a, b = map(int, input().split())
        if(a % 2 != 0 and b % 2 != 0):
            print(a * b // 2 + 1)
        else:
            print(a * b // 2)

except:
    pass

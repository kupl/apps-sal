# cook your dish here
test = int(input())
for t in range(test):
    n, l = input().split()
    n, l = int(n), int(l)
    if(n == 1):
        print(l)
    elif(n == 2):
        if(l % 2 == 0):
            print((l // 2) - 1)
        else:
            print((l // 2) - 2)
    else:
        print((l // n) - 1)

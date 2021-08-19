# cook your dish here
for i in range(int(input())):
    n = int(input())
    for i in range(n + 1):
        temp = i
        while(temp != 0):
            print("*", end="")
            temp -= 1
        print(i, end="")
        print()

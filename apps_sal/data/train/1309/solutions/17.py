for i in range(int(input())):
    n = int(input())
    for i in range(n, 0, -1):
        temp = i
        val = n - temp
        while(val != 0):
            print("*", end="")
            val -= 1

        while(temp != 0):
            print(temp, end="")
            temp -= 1

        print()

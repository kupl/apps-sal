for _ in range(int(input())):
    k = int(input())
    if k == 1:
        print("*")
    else:
        for a in range(k - 1):
            print(" ", end="")
        print("*")
        i = 2
        temp = k
        while(i < k):
            for m in range(temp - i):
                print(" ", end="")
            print("*", end="")
            for j in range(i + i - 3):
                print(" ", end="")
            print("*")
            i = i + 1

        for i in range(2 * k - 1):
            print("*", end="")
        print("\r")

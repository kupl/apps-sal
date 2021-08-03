for _ in range(int(input())):
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    k = int(input())
    for i in range(1, k + 1):
        if(i % 2 == 1):
            string = alphabets[:i]
            print(" " * (k - i), end="")
            print(string)
        else:
            print(" " * (k - i), end="")
            for j in range(1, i + 1):
                print(j, end="")
            print("")

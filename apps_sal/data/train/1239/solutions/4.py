# cook your dish here

t = int(input())

while t:
    rows = int(input())

    for i in range(0, rows):
        for j in range(rows - i):
            print(end=" ")

        for j in range(0, i + 1):
            print(rows - j, end="")
        print("")

    k = 0
    for i in range(rows + 1):
        for j in range(i):
            print(end=" ")
        for j in range(0, rows + 1 - k):
            print(rows - j, end="")

        print("")
        k += 1

    t -= 1

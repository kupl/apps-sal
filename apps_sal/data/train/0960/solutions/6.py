
for _ in range(int(input())):
    n = int(input())
    c = 1
    for i in range(0, n):
        for j in range(0, n):
            print(bin(c).replace("0b", ""), end=" ")
            c += 1

        print()

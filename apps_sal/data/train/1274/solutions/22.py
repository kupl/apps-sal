t = int(input())
for i in range(t):
    k = int(input())
    for j in range(1, k + 1):
        for k in range(1, k + 1):
            print(f"{k}{j}", end="")
        print()

t = int(input())
for k in range(0, t):
    n = int(input())
    if n == 1:
        x = int(input())
        g = int(input())
        if g == 1:
            print("Impossible")
        else:
            print("Possible")
    else:
        x = int(input())
        seq = input().split(" ")
        game = []

        for j in range(0, n):
            game.append(int(seq[j]))
        game.sort()

        if(game[0] == 1):
            print("Impossible")
        else:
            print("Possible")

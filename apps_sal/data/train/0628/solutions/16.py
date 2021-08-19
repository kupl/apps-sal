t = int(input())
for i in range(t):
    game = input()
    (x, y) = game.split('W')
    if len(x) == len(y):
        print('Chef')
    else:
        print('Aleksa')

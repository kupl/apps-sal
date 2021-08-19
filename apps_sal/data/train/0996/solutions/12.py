n = int(input())
p1 = 0
p2 = 0
lead = 0
winner = 0
for i in range(n):
    (player1, player2) = list(map(int, input().split()))
    p1 += player1
    p2 += player2
    if abs(p1 - p2) > lead:
        lead = abs(p1 - p2)
        if p2 > p1:
            winner = 2
        else:
            winner = 1
print(winner, lead)

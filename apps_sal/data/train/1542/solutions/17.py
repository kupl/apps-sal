t = int(input())
for z in range(t):
    n = int(input())
    board = input()
    b = list(board)
    maxscore = 0
    scores = list(map(int, input().split()))
    for i in range(0, n - 7):
        multiplier = 1
        score = 0
        for j in range(i, i + 8):
            if (board[j] == "."):
                score += scores[j - i]
            elif(board[j] == "d"):
                score += scores[j - i] * 2
            elif(board[j] == "t"):
                score += scores[j - i] * 3
            elif(board[j] == "T"):
                score += scores[j - i]
                multiplier *= 3
            else:
                score += scores[j - i]
                multiplier *= 2
        maxscore = max(maxscore, multiplier * score)
    print(maxscore)

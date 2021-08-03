for _ in range(int(input())):
    Score = [0] * 8
    for _ in range(int(input())):
        P, S = list(map(int, input().split()))
        if P >= 1 and P <= 8:
            if Score[P - 1] < S:
                Score[P - 1] = S
    print(sum(Score))

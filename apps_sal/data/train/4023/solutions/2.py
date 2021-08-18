def high(x):
    scoreboard = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    heck = x.split()
    score = 0
    score_final = 0
    big_word = []
    for each in heck:
        print(each)
        for every in each:
            if every in scoreboard:
                score = score + scoreboard.index(every) + 1
                print(score)
        if score > score_final:
            score_final = score
            big_word = each
            score = 0
        else:
            score = 0
    return big_word

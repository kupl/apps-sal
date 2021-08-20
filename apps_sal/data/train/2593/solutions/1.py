vowels = ['A', 'E', 'I', 'O', 'U']


def minion_game(string):
    score_kevin = 0
    score_stuart = 0
    for ind in range(len(string)):
        if string[ind] in vowels:
            score_kevin += len(string) - ind
        else:
            score_stuart += len(string) - ind
    if score_kevin > score_stuart:
        return 'Kevin ' + str(score_kevin)
    elif score_kevin < score_stuart:
        return 'Stuart ' + str(score_stuart)
    else:
        return 'Draw'

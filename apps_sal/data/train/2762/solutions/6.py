def scoreboard(string):
    scores = ['nil', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    arr = []
    temp = -1
    num = -1
    for score in scores:
        i = string.find(score)
        if i != -1:
            if string.find(score, i + 1) != -1:
                same = scores.index(score)
                arr = [same, same]
            elif temp != -1:
                if i > temp:
                    arr = [num, scores.index(score)]
                else:
                    arr = [scores.index(score), num]
            else:
                temp = i
                num = scores.index(score)
    return arr

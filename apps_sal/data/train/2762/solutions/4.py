from re import findall
score = {'nil': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}


def scoreboard(string):
    return list(map(score.get, findall('|'.join(score), string)))

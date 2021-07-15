def scoreboard(string):
    scores = {'nil': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    return [scores[x] for x in string.split() if x in scores]

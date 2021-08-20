import re
scores = {word: i for (i, word) in enumerate('nil one two three four five six seven eight nine'.split())}
pattern = re.compile('\\b({})\\b'.format('|'.join(scores)))


def scoreboard(string):
    return [scores[m] for m in pattern.findall(string)]

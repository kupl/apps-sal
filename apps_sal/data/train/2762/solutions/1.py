PTS = {w:i for i,w in enumerate('nil one two three four five six seven eight nine'.split())}

def scoreboard(s):
    return [PTS[w] for w in s.split()[-2:]]

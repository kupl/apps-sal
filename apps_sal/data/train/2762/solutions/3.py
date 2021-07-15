import re

d = {'nil':0,
     'one':1,
     'two':2,
     'three':3,
     'four':4,
     'five':5,
     'six':6,
     'seven':7,
     'eight':8,
     'nine':9}


def scoreboard(string):
    x = re.findall('nil|one|two|three|four|five|six|seven|eight|nine', string)
    return [d[x[0]], d[x[1]]]

def scoreboard(string):
    data = {
        "nil": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    return [data[word] for word in string.split() if word in data.keys()]

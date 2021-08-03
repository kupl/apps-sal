def scoreboard(string):
    words = string.split()
    result = []
    numMap = ['nil', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for word in words:
        if word in numMap:
            result.append(numMap.index(word))
    return result

def find_children(people):
    string = []
    answer = []
    symbol = ''
    index = -1
    dex = -1
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for lol in people:
        string.append(lol)
    symbol = ''
    index = -1
    dex = -1
    for nim in range(len(string)):
        dex = -1
        index += 1
        symbol = string[index]
        for num in range(len(alphabet)):
            dex += 1
            if alphabet[dex].find(symbol) != -1:
                break
        if dex <= 25:
            string[nim] = alphabet[dex + 26] + string[nim]
        else:
            string[nim] = string[nim] + string[nim]
    symbol = ''
    index = -1
    dex = -1
    string.sort()
    string = string + ['!!']
    for nam in range(len(string)):
        string[nam] = string[nam][1:]
    while symbol != '!':
        dex = -1
        index += 1
        symbol = string[index]
        if symbol == '?' or symbol == "!":
            continue
        for num in range(len(alphabet)):
            dex += 1
            if alphabet[dex].find(symbol) != -1:
                break
        if dex <= 25:
            for num in range(string.count(symbol)):
                answer.append(symbol)
            string = ' '.join([str(i) for i in string]).replace(alphabet[dex], '?').split(' ')
        else:
            answer.append(alphabet[dex])
    return (''.join([str(i) for i in answer]))


print(find_children("aabAB"))

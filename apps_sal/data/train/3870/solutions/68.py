def solve(s):
    spaces = []
    reversed = s

    #get spaces
    for index in range(len(reversed)):
        if reversed[index] == " ":
            spaces.append(index)
    print(spaces)

    #strip spaces
    reversed = reversed.replace(" ", "")

    #reverse
    reversed = reversed[::-1]

    #add spaces
    for space in spaces:
        print(reversed)
        reversed = f'{reversed[:space]} {reversed[space:]}'
    return reversed

def solve(s):
    spaces = []
    reversed = s

    for index in range(len(reversed)):
        if reversed[index] == " ":
            spaces.append(index)
    print(spaces)

    reversed = reversed.replace(" ", "")

    reversed = reversed[::-1]

    for space in spaces:
        print(reversed)
        reversed = f'{reversed[:space]} {reversed[space:]}'
    return reversed

def mastermind(game):
    colors = ['Red', 'Blue', 'Green', 'Orange', 'Purple', 'Yellow']
    answers = []
    confirmed = ['', '', '', '']
    possible = ['', '', '', '']
    not_a_color = 0
    for color in colors:
        answers.append(game.check([color, color, color, color]))
    i = 0
    while i < len(answers):
        if answers[i] == []:
            not_a_color = colors[i]
            i = len(answers)
        i += 1
    for (c, possible) in enumerate(answers):
        if possible:
            possible_color = colors[c]
            not_possible_color = not_a_color
            i = 0
            remaining = len(possible)
            while i < 4 and remaining > 0:
                possible = [possible_color if i == j else not_possible_color for j in range(4)]
                possible_answer = game.check(possible)
                if possible_answer[0] == 'Black':
                    confirmed[i] = possible_color
                    remaining -= 1
                i += 1
    game.check(confirmed)

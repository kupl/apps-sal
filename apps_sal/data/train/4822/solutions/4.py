from random import choice


def mastermind(game):
    colors = ["Red", "Blue", "Green", "Orange", "Purple", "Yellow"]
    answer = ''
    for i in range(60):
        my_choice = [choice(colors) for i in range(4)]
        answer = game.check(my_choice)

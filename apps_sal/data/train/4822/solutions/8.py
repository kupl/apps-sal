def mastermind(game):
    colors = ["Red", "Blue", "Green", "Orange", "Purple", "Yellow"]
    my_choice = [random.choice(colors), random.choice(colors), random.choice(colors), random.choice(colors)]
    answer = game.check(my_choice)
    if answer == ['Black', 'Black', 'Black', 'Black']:
        count_won += 1
        return 'WON'
    else:
        return

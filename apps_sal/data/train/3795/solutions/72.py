def combat(health, damage):
    # your code here
    all = health - damage

    if all > 0:
        return all
    else:
        return 0

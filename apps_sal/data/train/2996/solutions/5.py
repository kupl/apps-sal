def how_much_coffee(events):
    EVENTS = ('cat', 'dog', 'movie', 'cw')
    cups = 0
    for event in events:
        if event.lower() in EVENTS:
            if event.isupper():
                cups += 2
            elif event.islower():
                cups += 1
    if cups > 3:
        return 'You need extra sleep'
    return cups

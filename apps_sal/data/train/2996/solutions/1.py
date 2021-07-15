def how_much_coffee(events):
    activities = ["cw", "cat", "dog", "movie"]
    coffee = 0
    for e in events:
        if e.lower() in activities:
            if e == e.upper():
                coffee += 2
            else:
                coffee += 1
            if coffee > 3:
                return "You need extra sleep"
    return coffee

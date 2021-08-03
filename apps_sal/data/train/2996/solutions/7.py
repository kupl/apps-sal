def how_much_coffee(events):
    score = sum(1 if event in ("cw", "cat", "dog", "movie") else 2 if event in ("CW", "CAT", "DOG", "MOVIE") else 0 for event in events)
    return "You need extra sleep" if score > 3 else score

def naughty_or_nice(data):
    return 'Nice!' if sum((1 if day == 'Nice' else -1 for month in data.values() for day in month.values())) >= 0 else 'Naughty!'

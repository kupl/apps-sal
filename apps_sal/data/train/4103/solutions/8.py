def naughty_or_nice(data):
    nice_count = 0
    naughty_count = 0
    for (month, days) in data.items():
        for (date, status) in days.items():
            if status == 'Nice':
                nice_count += 1
            else:
                naughty_count += 1
    return 'Naughty!' if nice_count < naughty_count else 'Nice!'

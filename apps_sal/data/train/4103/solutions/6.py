def naughty_or_nice(data):
    return 'Nice!' if str(data).count('Nice') >= str(data).count('Naughty') else 'Naughty!'

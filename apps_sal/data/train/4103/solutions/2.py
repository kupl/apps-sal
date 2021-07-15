def naughty_or_nice(data):
    s = str(data)
    return 'Nice!' if s.count('Nice') >= s.count('Naughty') else 'Naughty!'

import json
def naughty_or_nice(data):
    s = json.dumps(data)
    return 'Nice!' if s.count('Nice') >= s.count('Naughty') else 'Naughty!'

import json


def naughty_or_nice(data):
    parsed_data = json.dumps(data)
    return 'Nice!' if parsed_data.count('Nice') >= parsed_data.count('Naughty') else 'Naughty!'

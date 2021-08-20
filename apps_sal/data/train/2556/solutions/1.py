import re


def __starting_point():
    string = input()
    match = re.search('([a-zA-Z0-9])\\1+', string)
    print(match.group(1) if match else -1)


__starting_point()

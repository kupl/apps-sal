import re
def bracket_buster(x):
    if type(x) != str:
        return 'Take a seat on the bench.'
    pat = r'\[.*?\]'

    results = [match[1:-1] for match in re.findall(pat,str(x))]

    if len(results) == 0:
        return 'Take a seat on the bench.'
    else:
        return results

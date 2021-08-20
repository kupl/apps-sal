def validate_rhythm(meter, score):
    if [c for c in score if c not in '|1248'] or meter[1] not in [1, 2, 4, 8]:
        return 'Invalid rhythm'
    bar = meter[0] * 8 / meter[1]
    l = [len(b) for b in score.replace('4', '88').replace('2', '8' * 4).replace('1', '8' * 8).split('|')]
    if all((i == bar for i in l)):
        return 'Valid rhythm'
    if l[0] + l[-1] == bar and all((i == bar for i in l[1:-1])):
        return 'Valid rhythm with anacrusis'
    return 'Invalid rhythm'

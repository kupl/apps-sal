layout = [' 0', '1', 'abc2', 'def3', 'ghi4', 'jkl5', 'mno6', 'pqrs7', 'tuv8', 'wxyz9']
D_LAYOUT = {l: i + 1 for touch in layout for i, l in enumerate(touch)}
DEFAULT = 1


def presses(phrase):
    return sum(D_LAYOUT.get(l, DEFAULT) for l in phrase.lower())

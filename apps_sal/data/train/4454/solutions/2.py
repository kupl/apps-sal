buttons = ['1', 'abc2', 'def3', 'ghi4', 'jkl5', 'mno6', 'pqrs7', 'tuv8', 'wxyz9', '*', ' 0', '#']


def getPresses(c):
    for button in buttons:
        if c in button:
            return button.index(c) + 1
    return 0


def presses(phrase):
    return sum((getPresses(c) for c in phrase.lower()))

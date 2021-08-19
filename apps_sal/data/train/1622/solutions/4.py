from collections import deque


def bowling_score(frames):
    score = 0
    next_two_rolls = deque([0, 0], 2)
    for (i, frame) in enumerate(reversed(frames.split())):
        for roll in reversed(frame):
            if roll == 'X':
                additional = sum(next_two_rolls) if i else 0
                score += 10 + additional
                next_two_rolls.appendleft(10)
            elif roll == '/':
                additional = next_two_rolls[0] if i else 0
                score += 10 + additional
                next_two_rolls.appendleft('/')
            else:
                if next_two_rolls[0] == '/':
                    next_two_rolls[0] = 10 - int(roll)
                else:
                    score += int(roll)
                next_two_rolls.appendleft(int(roll))
    return score

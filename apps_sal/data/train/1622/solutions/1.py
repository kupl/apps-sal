import re


def bowling_score(frames):
    frames = frames.split()
    score = 0

    for frame, roll in enumerate(frames, 1):
        if not roll.isdigit():
            if frame < 10:
                roll = (roll + "".join(frames[frame:]))[:3]

        score += sum(int(r) if r.isdigit() else 10 for r in re.sub("\d/", "X", roll))

    return score

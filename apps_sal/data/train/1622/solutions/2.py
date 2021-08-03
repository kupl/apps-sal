def frame2rolls(frame_line: str):
    rolls = []
    for i in range(len(frame_line)):
        if frame_line[i] == 'X':
            rolls.append(10)
        elif frame_line[i] == '/':
            rolls.append(10 - rolls[-1])
        elif frame_line[i] == ' ':
            continue
        else:
            rolls.append(int(frame_line[i]))
    return rolls


def bowling_score(frame_line: str) -> int:
    score = {i: 0 for i in range(10)}
    frames = frame_line.split(' ')
    rolls = frame2rolls(frame_line)
    r = 0
    for i in range(10):
        if i == 9:  # The last frame is special
            score[i] = sum(rolls[r:])
            break
        if frames[i] == 'X':
            score[i] = 10 + rolls[r + 1] + rolls[r + 2]
            r += 1
        elif frames[i][-1] == '/':
            score[i] = 10 + rolls[r + 2]
            r += 2
        else:
            score[i] = rolls[r] + rolls[r + 1]
            r += 2
    score = [score[f] for f in score]
    return sum(score)


def generate_frames() -> str:
    frames = []
    for i in range(10):
        roll1 = random.randint(0, 10)
        if roll1 == 10:
            frames.append('X')
        else:
            roll2 = random.randint(0, 10 - roll1)
            if roll2 + roll1 == 10:
                frames.append("%d/" % roll1)
            else:
                frames.append("%d%d" % (roll1, roll2))

    if frames[-1][-1] == 'X':
        f10_r2 = random.randint(0, 10)
        if f10_r2 == 10:
            f10_r3 = random.randint(0, 10)
            if f10_r3 == 10:
                frames[-1] = "XXX"
            else:
                frames[-1] = "XX%d" % f10_r3
        else:
            f10_r3 = random.randint(0, 10 - f10_r2)
            if f10_r2 + f10_r3 == 10:
                frames[-1] = "X%d/" % f10_r2
            else:
                frames[-1] = "X%d%d" % (f10_r2, f10_r3)
    elif frames[-1][-1] == '/':
        f10_r3 = random.randint(0, 10)
        if f10_r3 != 10:
            frames[-1] = "%s%d" % (frames[-1], f10_r3)
        else:
            frames[-1] = "%sX" % frames[-1]
    return ' '.join(frames)

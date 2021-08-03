def bowling_score(frames):
    score = frames.split(" ")
    total = 0
    for i in range(len(score) - 1):
        if calculate(score[i]) == 10:
            if "X" in score[i]:
                if len(score[i + 1]) == 1:
                    total += 10 + calculate(score[i + 1][0]) + calculate(score[i + 2][0])
                else:
                    total += 10 + calculate(score[i + 1][:2])
            else:
                total += 10 + calculate(score[i + 1][0])
        else:
            total += calculate(score[i])
    if len(score[-1]) == 2:
        return total + calculate(score[-1])
    return total + calculate(score[-1][:2]) + calculate(score[-1][2:])


def calculate(s):
    if "X" in s:
        return 10 * s.count("X")
    elif "/" in s:
        return 10
    return int(s[0]) + int(s[1]) if len(s) == 2 else int(s[0])

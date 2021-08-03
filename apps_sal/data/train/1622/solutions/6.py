def bowling_score(frames_main):
    frames = frames_main
    add = ""
    for i in range(0, len(frames_main) - 3):
        if frames_main[i] == '/':
            if frames_main[i - 1] == '0':
                frames = frames.replace('/', " " + 'V', 1)
                add += str(frames_main[i + 2]) + " "
                continue
            frames = frames.replace('/', " " + str(10 - int(frames_main[i - 1])), 1)
            add += str(frames_main[i + 2]) + " "

    frames = list(frames.split(' '))
    last = frames[len(frames) - 1]
    frames.remove(last)
    if last[1] == '/':
        if last[0] == '0':
            last = last.replace('/', 'V', 1)
        last = last.replace('/', str(10 - int(last[0])), 1)
    frames.append(last)
    string = "".join(frames)
    string = string.replace('', ' ')[1: -1]
    frames = list(string.split(" "))
    while '' in frames:
        frames.remove('')
    for i in range(0, len(frames) - len(last)):
        if frames[i] == 'X':
            add += frames[i + 1] + ' ' + frames[i + 2] + ' '
    add = list(add.split(" ")[0: -1])
    string = " ".join(frames) + " " + " ".join(add)
    string = string.replace('V', '10')
    string = string.replace('X', '10')
    frames = list(string.split(" "))
    while '' in frames:
        frames.remove('')
    return sum(list(map(int, frames)))

def look_and_say_sequence(e, n):
    for i in range(1, n):
        e = look_and_say(e)
    return e


def look_and_say(e):
    (current, count, seq) = (e[0], 0, '')
    for c in e:
        if c == current:
            count += 1
        else:
            seq += f'{count}{current}'
            (count, current) = (1, c)
    return seq + f'{count}{current}'

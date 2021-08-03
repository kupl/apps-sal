def elapsed_seconds(start, end):
    start = str(start).replace('-', ' ').replace(':', ' ').split(' ')
    end = str(end).replace('-', ' ').replace(':', ' ').split(' ')
    res = [int(end[i]) - int(start[i]) for i in range(6)]
    return res[2] * 86400 + res[3] * 3600 + res[4] * 60 + res[5]

def triangle(row):
    new_step = ''
    if len(row) == 1:
        return row
    while len(row) > 1:
        for i in range(1, len(row)):
            colors = ['R', 'G', 'B']
            if row[i - 1] == row[i]:
                new_step += row[i]
            else:
                colors.remove(row[i - 1])
                colors.remove(row[i])
                new_step += colors[0]
        if len(new_step) == 1:
            return new_step
        return triangle(new_step)

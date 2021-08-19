def blast_sequence(aliens, position):
    result = []
    aliens_lst = [[y, x, speed] for (x, row) in enumerate(aliens) for (y, speed) in enumerate(row) if speed != 0]
    time = 0
    while aliens_lst:
        for alien in aliens_lst:
            for _ in range(abs(alien[2])):
                if alien[0] == 0 and alien[2] < 0 or (alien[0] == len(aliens[0]) - 1 and alien[2] > 0):
                    alien[1] += 1
                    alien[2] *= -1
                    if alien[1] == position[0]:
                        return None
                else:
                    alien[0] += 1 if alien[2] > 0 else -1
        targets = [alien for alien in aliens_lst if alien[0] == position[1]]
        targets.sort(key=lambda alien: (alien[1], abs(alien[2]), alien[2]))
        if targets:
            target = targets.pop()
            aliens_lst.remove(target)
            result.append(time)
        time += 1
    return result

def artificial_rain(garden):
    output = []
    garden_cropped = []
    for i in range(len(garden) - 1):
        if garden[i] < garden[i + 1]:
            garden_cropped.append(+1)
        elif garden[i] > garden[i + 1]:
            garden_cropped.append(-1)
        else:
            garden_cropped.append(0)
    var = 0
    last_n = 1
    recent_zeros = 0
    for (idx, elem) in enumerate(garden_cropped):
        if elem == 1 and last_n == 1:
            last_n = 1
            var += 1
            recent_zeros = 0
        elif elem == 1 and last_n == -1:
            output.append(var + 1)
            last_n = 1
            var = 1 + recent_zeros
            recent_zeros = 0
        if elem == -1:
            last_n = -1
            var += 1
            recent_zeros = 0
        if elem == 0:
            var += 1
            recent_zeros += 1
    output.append(var + 1)
    return max(output) if len(garden) > 1 else 1

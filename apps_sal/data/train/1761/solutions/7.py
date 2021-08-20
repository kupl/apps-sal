def find(n):
    if n < 4:
        return [0, 1, 2, 2][n]
    (x, length, last_number, cycle, c) = (2, 2, 1, 2, [])
    for y in range(2, 10000):
        for i in range(cycle):
            length += x * y
            last_number += y
            if length >= n:
                while length > n:
                    length -= x
                    last_number -= 1
                    if length <= n:
                        return last_number + 1
            x += 1
        c.append(cycle)
        if cycle <= 3 and c.count(cycle) == 2:
            cycle += 1
        elif cycle <= 5 and c.count(cycle) == 3:
            cycle += 1
        elif cycle <= 8 and c.count(cycle) == 4:
            cycle += 1
        elif cycle <= 11 and c.count(cycle) == 5:
            cycle += 1
        elif cycle <= 15 and c.count(cycle) == 6:
            cycle += 1
        elif cycle <= 19 and c.count(cycle) == 7:
            cycle += 1
        elif cycle <= 23 and c.count(cycle) == 8:
            cycle += 1
        elif cycle <= 28 and c.count(cycle) == 9:
            cycle += 1
        elif cycle <= 33 and c.count(cycle) == 10:
            cycle += 1
        elif cycle <= 38 and c.count(cycle) == 11:
            cycle += 1
        elif cycle <= 44 and c.count(cycle) == 12:
            cycle += 1
        elif cycle <= 50 and c.count(cycle) == 13:
            cycle += 1
        elif cycle <= 56 and c.count(cycle) == 14:
            cycle += 1
        elif cycle <= 62 and c.count(cycle) == 15:
            cycle += 1
        elif cycle <= 69 and c.count(cycle) == 16:
            cycle += 1
        elif cycle <= 76 and c.count(cycle) == 17:
            cycle += 1
        elif cycle <= 83 and c.count(cycle) == 18:
            cycle += 1
        elif cycle <= 90 and c.count(cycle) == 19:
            cycle += 1
        elif cycle <= 98 and c.count(cycle) == 20:
            cycle += 1
        elif cycle <= 106 and c.count(cycle) == 21:
            cycle += 1

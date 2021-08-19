li = []
for i in range(2, 1000):
    for j in range(2, 20):
        li.append(i ** j)
li.sort()


def largest_power(n):
    found = [0, -1]
    for i in li:
        if i >= n:
            break
        if i > found[0]:
            found = [i, 1]
        elif i == found[0]:
            found[1] += 1
    return tuple(found) if n > 4 else (int(n != 1), -1)

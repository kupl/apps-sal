# This is not my code :,(
# I used those functions from here http://240hoursoflearning.blogspot.com/2017/09/the-calkin-wilf-tree.html
# Shame and dishonor on me :,(

def rat_at(n):
    # This is not my code :,(
    frac = [0, 1]
    n += 1
    nums = [n]

    while n > 0:
        n = n // 2
        nums.append(n)

    for n in reversed(nums):
        if n % 2 != 0:
            frac[0] += frac[1]

        else:
            frac[1] += frac[0]

    return tuple(frac)


def index_of(a, b):
    # This is not my code :,(
    if [a, b] == [1, 1]:
        return 0

    path = ''

    while [a, b] != [1, 1]:
        if a < b:
            b -= a
            path += '0'
        else:
            a -= b
            path += '1'
    addForDepth = 2**len(path) - 1

    return addForDepth + int(path[::-1], 2)

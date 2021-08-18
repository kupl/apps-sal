import re


def do_math(s):
    sortedArr = []
    unsortedArr = s.split()

    for i in range(ord('a'), ord('z') + 1):
        for item in unsortedArr:
            s = re.sub("\d+", "", item)
            if i == ord(s):
                sortedArr.append(re.sub("[a-z]", "", item))

    result = int(sortedArr[0])

    for i in range(len(sortedArr) - 1):
        op = (i + 4) % 4
        if op == 0:
            result += int(sortedArr[1 + i])
        elif op == 1:
            result -= int(sortedArr[1 + i])
        elif op == 2:
            result *= int(sortedArr[1 + i])
        else:
            result /= float(sortedArr[1 + i])

    return round(result)

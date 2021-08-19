import re


def do_math(s):
    sortedArr = []                                            # sort sorted items
    unsortedArr = s.split()                                   # split input into array items

    for i in range(ord('a'), ord('z') + 1):                   # evaluate items on the basis of their letter-value
        for item in unsortedArr:
            s = re.sub("\d+", "", item)
            if i == ord(s):
                sortedArr.append(re.sub("[a-z]", "", item))   # store only digits, "smaller" letters in ascii value = earlier

    result = int(sortedArr[0])

    for i in range(len(sortedArr) - 1):                        # use as int
        op = (i + 4) % 4                                       # mod to maintain operation order
        if op == 0:
            result += int(sortedArr[1 + i])
        elif op == 1:
            result -= int(sortedArr[1 + i])
        elif op == 2:
            result *= int(sortedArr[1 + i])
        else:
            result /= float(sortedArr[1 + i])                   # use float for division

    return round(result)                                      # return suggested round-value

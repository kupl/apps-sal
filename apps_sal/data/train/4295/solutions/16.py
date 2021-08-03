def balanced_num(number):
    if len(str(number)) == 1:
        return "Balanced"

    nlen = len(str(number))
    number = str(number)
    mid = nlen // 2
    left = right = 0

    for i in range(nlen - 1, mid, -1):
        right += int(number[i])

    if(nlen % 2 == 0):
        mid = mid - 1

    for i in range(0, mid):
        left += int(number[i])

    if left == right:
        return "Balanced"

    return "Not Balanced"

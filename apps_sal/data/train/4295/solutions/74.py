def balanced_num(number):
    num_str = str(number)
    length = len(num_str)
    middle = int(length // 2)

    if length % 2 == 0:
        left = 0
        right = 0
        for i in range(0, middle - 1, 1):
            left += int(num_str[i])
        for j in range(middle + 1, length, 1):
            right += int(num_str[j])
        if left == right:
            return "Balanced"
        else:
            return "Not Balanced"

    if length % 2 != 0:
        left = 0
        right = 0
        for i in range(0, middle, 1):
            left += int(num_str[i])
        for j in range(middle + 1, length, 1):
            right += int(num_str[j])
        if left == right:
            return "Balanced"
        else:
            return "Not Balanced"

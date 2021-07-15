def balanced_num(number):
    string = str(number)
    length = len(string)
    left = None
    right = None
    if length %2 == 0:
        left = string[:int(length/2) -1]
        right = string[int(length/2) +1:]
    else:
        left = string[:int(length/2)]
        right = string[int(length/2) +1:]
    sum_left = 0
    for i in left:
        sum_left = int(i) + sum_left
    sum_right = 0
    for j in right:
        sum_right = int(j) + sum_right
    if sum_left == sum_right:
        return "Balanced"
    else:
        return "Not Balanced"


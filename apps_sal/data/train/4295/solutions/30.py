def balanced_num(number):
    num_string = str(number)
    length = len(num_string)

    if length < 3:
        return "Balanced"

    split_at = length / 2 - 1 if length % 2 == 0 else length // 2

    sum_one = 0
    for num in num_string[: int(split_at)]:
        sum_one += int(num)
    
    sum_two = 0
    for num in num_string[-int(split_at) :]:
        sum_two += int(num)
    
    return "Balanced" if sum_one == sum_two else "Not Balanced"
